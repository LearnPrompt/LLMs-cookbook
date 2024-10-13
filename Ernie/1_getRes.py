import requests
import json

# 申请地址：https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application

API_KEY = "HuGwOlYEi03jPxSZuxLMfC1v"
SECRET_KEY = "huE3Kd2RB9Ra5oyd2k1MLorkkbTXOGIU"

def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    
    payload = json.dumps({
        "user_id": "1",
        "messages": [
            {
                "role": "user",
                "content": "你好，你能做什么呢？"
            },
        ],
        "temperature": 0.95,
        "top_p": 0.8,
        "penalty_score": 1
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()