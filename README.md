# Simple LLM Chat Interface

A minimalist chat application that uses LangChain with Ollama to interact with local LLM models.

## Features

- Context-aware conversations with LLM models
- Command-line interface for quick interactions
- Maintains conversation history
- Works with any Ollama-supported model (default: Llama 3.1)

## Prerequisites

- Python 3.8+
- Ollama installed locally (https://ollama.com)
- Llama 3.1 model pulled in Ollama (`ollama pull llama3.1`)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/SanthanaBharathiM/Chatbot-with-ollama
cd Chatbot-with-ollama
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install langchain-ollama langchain-core
```

## Usage

Run the script to start chatting:
```bash
python chat_app.py
```

Enter your messages and receive responses from the LLM. Type 'exit' to end the conversation.

## Customization

- Change the model by modifying the `model` parameter in the script
- Adjust the prompt template to change how the LLM responds
- Extend the code to save conversation history to a file

## Example Conversation

```
Welcome to conversation! Type 'exit' to quit.
You: What is machine learning?
AI: Machine learning is a subset of artificial intelligence that focuses on developing algorithms and statistical models that enable computers to perform tasks without explicit programming. Instead, these systems learn from data and improve their performance over time through experience.

You: Give me an example application
AI: An example application of machine learning is email spam filtering. The system learns from patterns in previously identified spam messages to recognize characteristics of unwanted emails. It analyzes features like specific words, sender information, and formatting patterns to make predictions about whether new incoming emails are spam or legitimate. As users continue to mark emails as spam or not spam, the system adapts and improves its accuracy over time.

You: exit
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
