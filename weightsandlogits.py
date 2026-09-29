import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load a compact causal language model and its tokenizer
model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
model.eval()

prompt = input(f"please put your prompt here :")
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    # outputs.logits shape: [batch_size, sequence_length, vocab_size]
    logits = outputs.logits

# Extract the logits corresponding strictly to the last token position``
next_token_logits = logits[0, -1, :]

# Retrieve the top 5 highest logit values and their corresponding token IDs
top_k_logits, top_k_indices = torch.topk(next_token_logits, k=5)

print(f"Vocab size: {next_token_logits.shape[0]}")
print(f"Logit range: min={next_token_logits.min().item():.2f}, max={next_token_logits.max().item():.2f}\n")

print("Top 5 candidates by raw logit score:")
for rank, (logit_val, token_id) in enumerate(zip(top_k_logits, top_k_indices), start=1):
    token_str = tokenizer.decode([token_id.item()])
    print(f"{rank}. Token ID: {token_id.item():<5} | Token: {repr(token_str):<12} | Logit: {logit_val.item():.3f}")