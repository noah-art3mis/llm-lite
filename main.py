# https://llm.datasette.io/en/stable/index.html

import llm
import os
import dotenv

# MODEL = "3.5"
MODEL = "mistral-7b-openorca"
PROMPT = "does the api key go inside quotes insite the .env file?"


def main():
    dotenv.load_dotenv()
    model = llm.get_model(MODEL)
    model.key = os.environ.get("LLM_OPENAI")
    response = model.prompt(PROMPT)
    print(response.text())


if __name__ == "__main__":
    main()
