import requests
import json
from urllib.parse import quote


data = {
    "sCLMID":"CLMKabuNewOrder",
    "sZyoutoekiKazeiC":"1",
    "sIssueCode":"8411",
    "sSizyouC":"00",
    "sBaibaiKubun":"3",
    "sCondition":"0",
    "sOrderPrice":"0",
    "sOrderSuryou":"1000",
    "sGenkinShinyouKubun":"0",
    "sOrderExpireDay":"0",
    "sGyakusasiOrderType":"0",
    "sGyakusasiZyouken":"0",
    "sGyakusasiPrice":"*",
    "sTatebiType":"*",
    "sTategyokuZyoutoekiKazeiC":"*",
    "sSecondPassword":"pswd",
}

json_string =json.dumps(data)
encoded_json_string = quote(json_string)

url = f'https://demo-kabuka.e-shiten.jp/e_api_v4r5/request/MzUzMDI0NzExMDcwMS0xMTYtNjAzMDU=/?{encoded_json_string}

response = requests.get(url)

print(response.text)