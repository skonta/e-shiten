import requests   #访问网页
import json       #处理json数据，网页返回的格式
from urllib.parse import quote    #URL编码

def get_market_price():
    url = "https://demo-kabuka.e-shiten.jp/e_api_v4r6/price/MTU2MzkyNTE4MjYwNS0xMTYtNDU4MDM=/"
    data = {
        "sCLMID": "CLMMfdsGetMarketPrice",
        "sTargetIssueCode": "6501,6502,6503",
        "sTargetColumn": "pDPP,tDPP:T,pPRP"
        }

json_string =json.dumps(data)
encoded_json_string = quote(json_string)

print(encoded_json_string)