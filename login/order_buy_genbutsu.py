import requests

url = "https://demo-kabuka.e-shiten.jp/e_api_v4r5/"

data = {
    "sCLMID":"CLMKabuNewOrder",
    "sZyoutoekiKazeiC":"1",
    "sIssueCode":"8411",
    "sSizyouC":"00",
    "sBaibaiKubun":"3",
    "sCondition":"0",
    "sOrderPrice":"0",
    "sOrderSuryou":"100",
    "sGenkinShinyouKubun":"0",
    "sOrderExpireDay":"0",
    "sGyakusasiOrderType":"0",
    "sGyakusasiZyouken":"0",
    "sGyakusasiPrice":"*",
    "sTatebiType":"*",
    "sTategyokuZyoutoekiKazeiC":"*",
    "sSecondPassword":"pswd",
}

response = requests.post(url, json=data)

response_json = response.json()
print(response_json)