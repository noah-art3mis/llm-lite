# llm-lite

Minimal implementation for running a LLM locally using [llm](https://llm.datasette.io/en/stable/index.html).

See https://simonwillison.net/2024/Apr/22/llama-3/

## How to use

1.  open a terminal at the root directory of the project.

    - you can do this on windows by opening explorer, clicking on the directory bar (the one that goes `C:\...` at the top of the window) and typing `cmd`.

1.  run the following commands

    1.  create virtual environment

            python -m venv venv

    1.  activate the virtual environment

            venv/Scripts/activate (windows)
            source venv/bin/activate (mac/linux)

    1.  install dependencies

            pip install llm
            llm install llm-gpt4all

1.  set parameters in `run_llm_locally.py`

    - model (SOTA right now is Llama 3)
    - prompt
    - temperature (for factual tasks, use 0.0)

1.  run the program

        python run_llm_locally.py

    - if you are running the model for the first time, it will download it first.
