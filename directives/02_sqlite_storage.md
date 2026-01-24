# Ticket 02: SQLite Storage Layer

**Objective**: Create a persistent storage layer using SQLite to save the market data (Klines) retrieved from Binance.

## Functional Specifications

1.  **File**: `app/storage/db.py`
2.  **Dependencies**: `sqlite3` (native), `pandas`
3.  **Functions**:
    - `get_db_connection()`: Returns a context manager or connection object to `market_data.db`.
    - `init_db()`: Creates the `klines` table if it doesn't exist.
    - `save_klines(df: pd.DataFrame)`: Inserts the DataFrame into the database.

## Database Schema (Table: `klines`)

| Column      | Type     | Constraint  |
| :---------- | :------- | :---------- |
| `timestamp` | DATETIME | PRIMARY KEY |
| `open`      | REAL     |             |
| `high`      | REAL     |             |
| `low`       | REAL     |             |
| `close`     | REAL     |             |
| `volume`    | REAL     |             |

## Technical Details

- **Efficient Upsert**: Use `INSERT OR IGNORE` or pandas `to_sql` with conflict handling to avoid crashing on duplicate timestamps.
- **Data Integrity**: Ensure the `timestamp` is stored correctly (SQLite doesn't have a native specialized Date type, it stores strings or numbers. Storing standard ISO8601 strings is recommended for readability).
- **Transformation**: The DataFrame index (`timestamp`) must be pushed as a column.

## Success Criteria
- Running `init_db()` creates a `market_data.db` file.
- `save_klines(df)` saves data without errors.
- Rerunning `save_klines(df)` with the same data does not create duplicates nor crash.
