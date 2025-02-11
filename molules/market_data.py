import requests

def get_market_data(crypto_ids):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url).json()
    data = []
    for crypto, info in response.items():
        data.append({
            "Criptomoeda": crypto,
            "Preço (USD)": info["usd"],
            "Variação 24h (%)": round(info.get("usd_24h_change", 0), 2)
        })
    return data
