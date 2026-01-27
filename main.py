from app.ingestion.binance_client import fetch_klines
import app.storage.db as db
import pandas as pd

def run_pipeline():
    db.init_db()

    symbol = "BTCUSDT"
    interval = "1h"
    
    print(f"Starting ingestion for {symbol} ({interval})...")

    try:
        df = fetch_klines(symbol, interval)
        print(f"Fetched {len(df)} rows.")
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    try:
        db.save_klines(df)
        print("Data successfully saved to SQlite")
    except Exception as e:
        print(f"Error saving data: {e}")


if __name__ == "__main__":
    run_pipeline()
    