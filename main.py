# https://llm.datasette.io/en/stable/index.html

import llm
import os
import dotenv

MODEL = "mistral-7b-openorca"
PROMPT = (
    "is this working? you are not gpt-3 nor are you trained by openai. you are mistral"
)


def main():
    dotenv.load_dotenv()
    model = llm.get_model(MODEL)
    model.key = os.environ.get("LLM_OPENAI")
    response = model.prompt(PROMPT)
    print(response.text())


if __name__ == "__main__":
    main()
