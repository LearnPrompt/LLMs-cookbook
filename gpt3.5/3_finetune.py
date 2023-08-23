import requests

url = "https://api.openai.com/v1/fine_tuning/jobs"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}
data = {
    "training_file": "file-lYTyREfNrFCCsybGVluzJE18",
    "model": "gpt-3.5-turbo-0613"
}

response = requests.post(url, headers=headers, json=data)
print(response.text)