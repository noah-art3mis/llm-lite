# llm-lite

Minimal implementation for running a LLM locally.

Uses [llm](https://llm.datasette.io/en/stable/index.html) and Mistral-7B.

## Instructions

1. open a terminal at the root directory of the project.

    - you can do this on windows by opening explorer, clicking on the directory bar (the one that goes `C:\...` at the top of the window) and typing `cmd`. Alternatively you can open a terminal window in VSCode with the command `CTRL  + '`.

1. run the following commands

    1. create virtual environment

        `python -m venv venv`

    1. activate the virtual environment

        `venv/Scripts/activate` (windows)
        `source venv/bin/activate` (mac)

    1. install dependencies

        `python install -r requirements.txt`

    1. (optional) if you want to run chatgpt (non-locally) do `echo 'LLM_OPENAI="your_api_key_here"' > .env`. now it knows your key. go into `main.py` and change the model (chatgpt is `"chatgpt"`).

1. set the prompt in `main.py`

1. run the program

    `python main.py`
