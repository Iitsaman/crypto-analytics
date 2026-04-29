import requests
import pandas as pd

def get_crypto_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": 30
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    prices = data.get("prices", [])
    volumes = data.get("total_volumes", [])

    if not prices:
        return pd.DataFrame()

    df = pd.DataFrame({
        "timestamp": [p[0] for p in prices],
        "price": [p[1] for p in prices],
        "volume": [volumes[i][1] if i < len(volumes) else None for i in range(len(prices))]
    })

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["coin"] = coin_id

    return df