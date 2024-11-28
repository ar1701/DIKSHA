
from llmware.prompts import Prompt
from llmware.models import ModelCatalog

# models = ModelCatalog().list_all_models()

# for m in models:
#     print(m['model_name'])

# exit()

# model = ModelCatalog().load_model("gpt-4o-mini",
#                                   )

res = model.stream(
    "What is newton 1st law of motion?")
for c in res:
    print(c)
# res["llm_response"] = res["llm_response"].split("<|im_end|>")[0]
# print(res)
