import requests
h = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}
d = {
    "model": "text-davinci-003",
    "prompt": "我在体检是正常的，但是去献血医生最是说我的血压高，不能献。血压是130、80这是为什么呢？",
    "max_tokens": 100,
    "temperature": 0
}
u = 'https://api.openai.com/v1/completions'
r = requests.post(url=u, headers=h, json=d, verify=False).json()
if 'choices' in r:
    print(r['choices'][0]['text'])