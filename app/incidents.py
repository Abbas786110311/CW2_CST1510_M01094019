import pandas as pd


def migrate_datasets_metadata():
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    data = pd.read_csv('DATA/cyber_incidents.csv')
    data.to_sql('cyber_incidents', conn)


    