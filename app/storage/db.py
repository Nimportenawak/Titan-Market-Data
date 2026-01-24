import sqlite3
import pandas as pd
import sqlite3

def get_db_connection():
    con = sqlite3.connect("market_data.db")
    return con


def init_db():
    con = get_db_connection()
    cur = con.cursor()
    cur.executem(
        '''
            CREATE TABLES IF NOT EXISTS klines (
                timestamp DATETIME PRIMARY KEY,
                open REAL, 
                high REAL,
                low REAL,
                close REAL,
                volume REAL,
            )
        '''
    )
    con.commit()
    con.close()