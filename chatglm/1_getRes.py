import zhipuai

zhipuai.api_key = "you api-key"
response = zhipuai.model_api.sse_invoke(
    model="chatglm_std",
    prompt=[
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "我是人工智能助手"},
        {"role": "user", "content": "你叫什么名字"},
        {"role": "assistant", "content": "我叫chatGLM"},
        {"role":"user", "content": "你都可以做些什么事"},
    ],
    temperature=0.95,
    top_p=0.7,
    incremental=True
)

response_lst = []

for event in response.events():
    if event.event == "add":
        print(event.data)
        response_lst.append(event.data)
    elif event.event == "error" or event.event == "interrupted":
        print(event.data)
    elif event.event == "finish":
        print(event.data)
        print(event.meta)
    else:
        print(event.data)


print("".join(response_lst))
# print(response_lst)