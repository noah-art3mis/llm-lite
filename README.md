# llm-lite

Minimal implementation for running a LLM locally.

Uses [llm](https://llm.datasette.io/en/stable/index.html) and Mistral-7B.

## Instructions

`python -m venv venv`

`python install -r requirements.txt`

`python main.py`

if you want to run chatgpt (non-locally) do

`echo 'LLM_OPENAI="your_api_key_here"' > .env`

and change `MODEL` to `"3.5"`
