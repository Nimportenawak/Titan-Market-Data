import requests
import pandas as pd

BASE_URL = "https://api.binance.com/api/v3/klines"

def fetch_klines(symbol: str, interval: str, limit: int = 1000)-> pd.DataFrame:

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    df = df.iloc[:, :6]
    df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
    cols_to_convert = ["open", "high", "low", "close", "volume"]
    df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    return df

if __name__ == "__main__":
    print(fetch_klines("BTCUSDT", "1h").head())
