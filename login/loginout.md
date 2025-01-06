import requests
import datetime

url = "https://demo-kabuka.e-shiten.jp/e_api_v4r5/auth/?
{
    "p_no": "1",
    "p_sd_date": datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S.%f")[:-3],
    "sCLMID": "CLMAuthLoginRequest",
    "sUserId": "hcw05193",  
    "sPassword": "Konta9323",
    "sJsonOfmt": "1"
}



response = requests.post(url, json=data)

print(response.text)
