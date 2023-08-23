import requests
import openai

url = "https://api.openai.com/v1/files"
headers = {
    "Authorization": "Bearer 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"
}

payload = {
    "purpose": "fine-tune",
}
files = {
    "file": open("/Users/lhj/AI/openai_cookbook/output.jsonl", "rb")
}

response = requests.post(url, headers=headers, data=payload, files=files)
print(response)

openai.api_key = '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'
print(openai.File.list())