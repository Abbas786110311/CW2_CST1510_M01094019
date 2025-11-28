import sqlite3
import pandas as pd


def create_user_table(conn):
    curr = conn.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        );
    """
    curr.execute(sql)
    conn.commit()


def add_user(conn, name, hash_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    parram = (name, hash_password)
    curr.execute(sql, parram)
    conn.commit()


def migrate_users(conn):
    with open('DATA/user.txt', 'r') as f:
        users = f.readlines()

    for user in users:
        name, hash_value = user.strip().split(',')
        add_user(conn, name, hash_value)


def get_all_users():
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    curr = conn.cursor()
    sql = "SELECT * FROM users"
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return users


def get_user(name_):
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = (name_,)
    curr.execute(sql, param)
    user = curr.fetchone()
    conn.close()
    return user


def migrate_datasets_metadata():
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    data = pd.read_csv('DATA/datasets_metadata.csv')
    data.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    conn.close()


def get_all_users_pandas():
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    sql = "SELECT * FROM datasets_metadata"
    data = pd.read_sql(sql, conn)
    print(data)
    conn.close()





from app.datasets import get_all_datasets_metadata
from app.db import conn

print(get_all_datasets_metadata(conn))







