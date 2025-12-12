import sqlite3
from app.db import get_db_connection


def add_user(conn, username, password_hash):
    curr = conn.cursor()
    sql = "INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)"
    params = (username, password_hash)
    curr.execute(sql, params)
    conn.commit()


def get_user(conn, username):
    curr = conn.cursor()
    sql = "SELECT id, username, password_hash FROM users WHERE username = ?"
    curr.execute(sql, (username,))
    return curr.fetchone()


def ensure_user_table(conn=None):
    if conn is None:
        conn = get_db_connection()
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
