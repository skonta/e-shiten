import requests
import json
from urllib.parse import quote
from datetime import datetime

data ={ 
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

print(response.text)

