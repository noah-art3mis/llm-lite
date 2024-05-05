import llm
import time

MODEL = "Meta-Llama-3-8B-Instruct"
PROMPT = "Three great names for a pet emu"
TEMPERATURE = 0.0


def main():
    print("Querying LLM...")
    start = time.perf_counter()

    model = llm.get_model(MODEL)
    response = model.prompt(
        PROMPT,
        temp=TEMPERATURE,
    )

    print(response.text())
    end = time.perf_counter()
    print(f"Took {end - start :0.2f} seconds")


if __name__ == "__main__":
    main()
