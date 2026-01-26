# Ticket 03: Ingestion Pipeline Script

**Objective**: Create the main entry point (`main.py`) to orchestrate the full data pipeline: Fetch from Binance -> Save to SQLite.

## Functional Specifications

1.  **File**: `main.py` (Project Root)
2.  **Dependencies**: `app.ingestion.binance_client`, `app.storage.db`
3.  **Flow**:
    - Initialize database (`db.init_db()`).
    - Fetch Klines for a specific symbol (e.g., BTCUSDT) and interval (e.g., 1h).
    - Save the data to SQLite (`db.save_klines()`).
    - Print a summary message (e.g., "Imported X rows for BTCUSDT").

## Technical Details

- **Error Handling**: Wrap the process in a `try/except` block to catch network or DB errors gracefully.
- **Command Line Args (Optional for now)**: Hardcode "BTCUSDT" and "1h" for this MVP, or use `argparse` if we want to be fancy (let's stick to hardcoded for MVP).

## Success Criteria
- Running `python main.py` populates the database with fresh data.
- User sees a clear success message in the console.
