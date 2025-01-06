import requests
import datetime

url = 'https://demo-kabuka.e-shiten.jp/e_api_v4r5/auth/?{"p_no": "1","p_sd_date": "2025.01.06-19:26:35.000","sCLMID": "CLMAuthLoginRequest","sUserId": "hcw05193",  "sPassword": "Konta9323","sJsonOfmt": "5"}'



response = requests.get(url)

print(response.text)

