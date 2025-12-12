import pandas as pd
import os


def migrating_cyber_incidents(conn=None):
    """Load cyber incidents CSV and optionally persist to the DB.

    Args:
        conn: optional DB connection/engine used with pandas.DataFrame.to_sql

    Returns:
        pandas.DataFrame
    """
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DATA', 'cyber_incidents.csv')
    df = pd.read_csv(csv_path)

    if conn is not None:
        try:
            df.to_sql('cyber_incidents', conn, if_exists='replace', index=False)
        except Exception:
            pass

    return df


