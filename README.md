# Mr.Helper

[![Build Status](https://img.shields.io/badge/build-manual-lightgrey)](https://example.com) [![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Mr.Helper is a lightweight, offline-capable AI chat assistant built with Streamlit that uses a locally-hosted Ollama model for responses.

## Table of Contents

- **Overview:** What this app does
- **Features:** Key capabilities
- **Tech Stack:** Languages and libraries used
- **Quick Start:** Install and run instructions
- **Configuration:** What you need to configure (Ollama)
- **Usage:** How to use the chat UI
- **Development & Testing:** Running locally and tests
- **Contributing & License:** How to help and legal

## Overview

`Mr.Helper` provides a simple chat UI (Streamlit) that sends conversation history to a locally running Ollama engine and displays model replies. It is designed to work without internet access once Ollama and the chosen model are available locally.

## Features

- Local AI chat using Ollama models (no internet required at runtime)
- Simple Streamlit chat UI with session-state conversation memory
- Uses the `llama3.2:1b` model by default (configurable in code)

## Tech Stack

- **Language:** Python 3.10+
- **UI:** Streamlit
- **Local LLM runtime:** Ollama

## Quick Start

### Prerequisites

- Install Ollama and ensure the Ollama daemon is running locally. Install the model referenced in the app (`llama3.2:1b`) or update the model name in the script.
- Python 3.10+ and Git (optional).

If you haven't installed the model locally, consult Ollama's docs. A typical command (see Ollama docs) may look like:

```bash
ollama pull llama3.2:1b
```

### Install

1. Clone the repo (or copy files into a folder):

```bash
git clone https://example.com/your-repo.git
cd your-repo
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### Run the app

Start the Streamlit app:

```bash
streamlit run Untitled-1.py
```

Open the URL shown by Streamlit (usually http://localhost:8501) and start chatting.

## Configuration

- No environment variables are required by the script. Ensure Ollama is running and the model in use (`llama3.2:1b`) is available locally. To change the model, edit the `model` argument in `ollama.chat(...)` inside `Untitled-1.py`.

## Usage

- Type queries in the Streamlit chat input box and press Enter.
- Conversation history persists for the current Streamlit session.

## Development & Testing

- The app is a single-file Streamlit app. Edit `Untitled-1.py` to change behavior (model, prompt handling, UI labels).
- There are no automated tests included by default.

## Contributing

- Open issues or PRs for improvements. For UI changes, keep them simple and self-contained.

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Authors & Contact

- **Author:** Srijit

---
