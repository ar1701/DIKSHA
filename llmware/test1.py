
from llmware.prompts import Prompt

prompter = Prompt().load_model("tiny-llama-chat-gguf")

res = prompter.prompt_main(
    "What is newton 1st law of motion?",)
res["llm_response"] = res["llm_response"].split("<|im_end|>")[0]
print(res["llm_response"])
