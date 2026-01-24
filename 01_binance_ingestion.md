# Ticket 01: Binance Ingestion Client

**Objective**: Implement an HTTP client to fetch historical price data (Klines/Candlesticks) from the Binance public API and return a clean DataFrame.

## Functional Specifications

1.  **File**: `app/ingestion/binance_client.py`
2.  **Dependencies**: `requests`, `pandas`
3.  **Main Function**:
    ```python
    def fetch_klines(symbol: str, interval: str, limit: int = 1000) -> pd.DataFrame:
        ...
    ```

## Technical Details

1.  **API Endpoint**: `GET https://api.binance.com/api/v3/klines`
2.  **Parameters**:
    - `symbol` (e.g., "BTCUSDT")
    - `interval` (e.g., "1h", "15m")
    - `limit` (max 1000)
3.  **Data Processing**:
    - The API returns a list of lists.
    - Columns to keep: Index 0 to 5 (`Open time`, `Open`, `High`, `Low`, `Close`, `Volume`).
    - **Renaming**: `timestamp`, `open`, `high`, `low`, `close`, `volume`.
    - **Typing**:
        - `timestamp` -> `datetime` (unit ms).
        - `open`, `high`, `low`, `close`, `volume` -> `float`.
    - **Index**: Set `timestamp` as the DataFrame index.

## Success Criteria
- The script `app/ingestion/binance_client.py` is executable standalone (via `if __name__ == "__main__":`) for testing.
- It displays the first 5 rows of a test call on BTCUSDT.
