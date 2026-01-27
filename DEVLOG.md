# DEVLOG

## [2026-01-24] Initialization & Binance Ingestion

### Achieved
- Set up project structure (directives, app, storage).
- Implemented Binance ingestion client (`app/ingestion/binance_client.py`).
- Used `pandas` to transform raw lists into a typed and indexed DataFrame.
- Merged `ingestion-binance` feature into `main`.

### Learned
- **Pandas**: `iloc` for slicing, `to_datetime` with `unit='ms'`, and `set_index`.
- **Git**: Branch management (fixed local/remote divergence with `pull --no-rebase`).
- **SQLite**: Distinction between `Connection` (the highway) and `Cursor` (the truck/storekeeper).
- **Architecture**: NEVER close the connection (`con.close()`) inside an insertion loop that reuses the cursor.

## [2026-01-26] SQLite Storage

### Achieved
- implemented `app/storage/db.py`.
- Created `klines` table with `init_db`.
- `save_klines` function with duplicate handling (`INSERT OR IGNORE`).

### Learned
- **Pandas Index**: Warning, `set_index("timestamp")` removes the `timestamp` column from the data (`row`). Must use the `index` variable in the iteration (`iterrows`).
- **SQLite Typing**: SQLite is permissive but the Python `sqlite3` driver does not know how to convert a `pandas.Timestamp` object.
    - *Error*: `InterfaceError: Error binding parameter...`
    - *Fix*: Explicitly convert: `str(index)`.
- **SQL**: `INSERT OR IGNORE` makes the script idempotent (re-runnable without unique constraint errors).