import openai
import os
import json

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
models = client.models.list()

# Save to JSON
with open("openai-models.json", "w") as f:
    json.dump([m.model_dump() for m in models.data], f, indent=4)

# Print models
for model in models.data:
    print("Model ID:", model.id)
    print("Owned by:", model.owned_by)
    print("-------------------")
