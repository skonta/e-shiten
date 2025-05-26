import requests
import json
from urllib.parse import quote
from datetime import datetime

def login():
    data = {
        "p_no": "2",
        "p_sd_date":datetime.now().strftime("%Y.%m.%d-%H:%M:%S.%f")[:-3],
        "sCLMID": "CLMAuthLoginRequest",
        "sUserId": "hcw05193",  
        "sPassword": "Konta9323",
        "sJsonOfmt": "5"
    }


    json_string =json.dumps(data)
    encoded_json_string = quote(json_string)


    url = f'https://demo-kabuka.e-shiten.jp/e_api_v4r6/auth/?{encoded_json_string}'


    response = requests.get(url)

    try:
        result = response.json()
        return result.get("sUrlPrice")  # 只返回仮想URL
    except Exception as e:
        print("登录失败:", e)
        return None

    print(response.text)


print(login())