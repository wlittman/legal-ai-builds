import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

response = client.chat.completions.create(
    model="gpt-4-deployment",
    messages=[{"role": "user", "content": "hello"}],
)

ENDPOINT = "https://my-resource.openai.azure.com/"
