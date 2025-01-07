import requests
import json
from urllib.parse import quote

data ={ 
    "p_no": "2",
    "p_sd_date": "2025.01.07-12:11:35.000",
    "sCLMID": "CLMAuthLoginRequest",
    "sUserId": "hcw05193",  
    "sPassword": "Konta9323",
    "sJsonOfmt": "5"
    }

json_string =json.dumps(data)
encoded_json_string = quote(json_string)


url = f'https://demo-kabuka.e-shiten.jp/e_api_v4r5/auth/?{encoded_json_string}'


response = requests.get(url)

print(response.text)

