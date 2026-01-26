from datetime import datetime
import sqlite3
import pandas as pd

def get_db_connection():
    con = sqlite3.connect("market_data.db")
    return con


def init_db():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(
        '''
            CREATE TABLE IF NOT EXISTS klines (
                timestamp TEXT,
                open REAL, 
                high REAL,
                low REAL,
                close REAL,
                volume REAL
            )
        '''
    )
    con.commit()
    con.close()


def save_klines(df: pd.DataFrame):
    con = get_db_connection()
    cur = con.cursor()

    for index, row in df.iterrows():
        cur.execute(
            '''
            INSERT OR IGNORE INTO klines(timestamp, open, high, low, close, volume) VALUES (?,?,?,?,?,?)
            ''',
            (str(index), row['open'], row['high'], row['low'], row['close'], row['volume'])
        )
    
    con.commit()
    con.close()


if __name__ == "__main__":
    init_db()
    print("Base de données initialisée.")
