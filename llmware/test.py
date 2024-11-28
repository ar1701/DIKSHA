from llmware.models import ModelCatalog
from llmware.gguf_configs import GGUFConfigs

# Configure the GGUF models
GGUFConfigs().set_config("max_output_tokens", 500)

def simple_chat_terminal(model_name):
    print(f"Simple Chat with {model_name}\n")
    print("Type 'exit' to end the chat.\n")

    # Load the model
    model = ModelCatalog().load_model(model_name, temperature=0.3, sample=True, max_output=450)

    # Initialize chat history
    chat_history = []

    while True:
        # User input
        prompt = input("You: ")
        if prompt.lower() == "exit":
            print("Chat ended. Goodbye!")
            break

        # Display user's input
        chat_history.append({"role": "user", "content": prompt})

        # Generate and display the assistant's response
        print("Assistant: ", end="", flush=True)
        response_generator = model.stream(prompt)  # Stream the bot's response
        bot_response = ""

        for chunk in response_generator:
            print(chunk, end="", flush=True)  # Real-time response
            bot_response += chunk

        print("\n")  # Add a newline for better readability

        chat_history.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    # List of chat models available
    chat_models = [
        "phi-3-gguf",
        "llama-2-7b-chat-gguf",
        "llama-3-instruct-bartowski-gguf",
        "openhermes-mistral-7b-gguf",
        "zephyr-7b-gguf",
        "tiny-llama-chat-gguf"
    ]

    # Select the first model as default (can be changed to another)
    model_name = chat_models[0]

    # Run the terminal chat application
    simple_chat_terminal(model_name)
