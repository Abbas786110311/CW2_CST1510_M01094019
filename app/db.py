import sqlite3
import os


def get_db_connection():
    """Return a sqlite3 connection to the project's database file.

    Uses the `DATA/intelligence_platform.db` path (matches other modules).
    """
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DATA', 'intelligence_platform.db')
    # Fallback: if that path doesn't exist, try upper/lowercase variations
    if not os.path.exists(db_path):
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'intelligence_platform.db')
    conn = sqlite3.connect(db_path)
    return conn
