import requests
import json

def coingecko_data():
    url = "https://api.coingecko.com/api/v3/global"

    headers = {
        "accept": "application/json",
        "x-cg-api-key": "CG-4htVhttjYyUpNUiTFgtF9ZXp"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def create_json ():
    market_data = coingecko_data()

    with open("market_data.json", "w", encoding="utf-8") as archive:
        json.dump(market_data, archive, indent=4, ensure_ascii=False)

    print("✅ market_data.json created !!!")  

#create_json()
