🧠 Logit Simulator

A simple interactive Logit Simulator that helps visualize what happens inside a language model after you enter a prompt.

The simulator takes a text prompt as input and demonstrates how a language model produces logits for possible next tokens, modifies them using different sampling techniques, and eventually selects the next token.

✨ Features
📝 Enter your own prompt
🧠 Simulate next-token prediction
📊 Visualize token logits
🔢 Compare logits and probabilities
🎯 Explore token selection
⚙️ Experiment with sampling parameters
🔥 Understand temperature
🔝 Experiment with Top-K
🌊 Experiment with Top-P / Nucleus Sampling
🔁 Explore repetition penalties and other logit modifications
🔍 What Are Logits?

Before a language model selects the next token, it produces a numerical value called a logit for every token in its vocabulary.

For example:

Prompt:
"The sky is"

Possible next tokens:

blue      → 8.42
beautiful → 6.91
dark      → 5.37
green     → 3.82
car       → 1.24

Higher logits indicate that the model considers a token more likely relative to other tokens.

The logits are then converted into probabilities using softmax:

P(token) = exp(logit) / Σ exp(all logits)

The simulator helps make this process easier to understand visually.

🔄 How It Works

The basic generation pipeline is:

                 ┌───────────────┐
                 │     Prompt    │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Tokenization  │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │  Model Pass   │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │     Logits    │
                 └───────┬───────┘
                         ↓
              ┌─────────────────────┐
              │ Logit Modifications │
              │ Temperature / etc. │
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │ Top-K / Top-P       │
              │ Filtering           │
              └──────────┬──────────┘
                         ↓
                 ┌───────────────┐
                 │ Token Sampling│
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Next Token    │
                 └───────────────┘
