from llmware.models import ModelCatalog
from llmware.prompts import Prompt
from llmware.gguf_configs import GGUFConfigs

# Configure the GGUF models
GGUFConfigs().set_config("max_output_tokens", 500)


def simple_chat_terminal(model_name):
    print(f"Simple Chat with {model_name}\n")
    print("Type 'exit' to end the chat.\n")

    try:
        # Load the model with explicit path
        model = Prompt().load_model(
            model_name,
            temperature=0.0,
            sample=False,
            max_output=450,  # Specify local model path
        )
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    chat_history = []
    while True:
        try:
            prompt = input("You: ")
            if prompt.lower() == "exit":
                print("Chat ended. Goodbye!")
                break

            # chat_history.append({"role": "user", "content": prompt})
            print("Assistant: ", end="", flush=True)

            response_generator = model.prompt_main(prompt)['llm_response']

            # response_generator = response_generator.split(
            #    "<|im_end|>", 1)[1].split("<|assistant|>", 1)[0]

            print(response_generator, end="")

            print("\n")
            prompt = ""
            # chat_history.append({"role": "assistant", "content": bot_response})

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break


if __name__ == "__main__":
    chat_models = [
        "phi-3-gguf",
        "llama-2-7b-chat-gguf",
        "llama-3-instruct-bartowski-gguf",
        "openhermes-mistral-7b-gguf",
        "zephyr-7b-gguf",
        "tiny-llama-chat-gguf"
    ]

    model_name = chat_models[0]
    simple_chat_terminal(model_name)
