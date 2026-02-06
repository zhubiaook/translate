# Translate CLI

A powerful AI-powered translation and chat CLI tool built with Python.

## Features

- **CLI Mode**: Quick translation or queries directly from the command line.
- **Interactive Mode**: Conversational interface for continuous interaction.
- **Streaming Responses**: Real-time token streaming for fast feedback.
- **Configurable**: Support for custom OpenAI-compatible API endpoints (e.g., DeepSeek).

## Prerequisites

- Python 3.12 or higher
- An API Key for an OpenAI-compatible provider (default is DeepSeek)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd translate
   ```

2. **Install dependencies:**
   Using `uv` (recommended):
   ```bash
   uv sync
   ```
   Or using pip:
   ```bash
   pip install -e .
   ```

## Configuration

You can configure the tool using environment variables. Create a `.env` file in the project root or export them in your shell.

| Variable          | Description                 | Default                    |
| ----------------- | --------------------------- | -------------------------- |
| `OPENAI_API_KEY`  | **Required.** Your API Key. | None                       |
| `OPENAI_BASE_URL` | The API Base URL.           | `https://api.deepseek.com` |
| `OPENAI_MODEL`    | The model to use.           | `deepseek/deepseek-chat`   |

## Usage

### 1. Command Line Arguments

Run a single query by passing arguments directly:

```bash
translate "Translate 'Hello world' to French"
```

### 2. Interactive Mode

Run without arguments to enter the interactive chat mode:

```bash
translate
```

Output:

```
Type 'quit' or 'exit' to exit.

> Hello
Hello! How can I help you today?
--------------------------------------------------

> quit
Goodbye! 👋
```

## Development

To run the locally during development:

```bash
# Run via uv
uv run translate
```

Or directly via python if installed in the environment:

```bash
python -m src.translate.main
```
