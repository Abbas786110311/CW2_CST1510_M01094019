import bcrypt
import sqlite3
import pandas as pd

password = 'Magic123'

def hash_password(password):
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(binary_password, salt)
    return hashed.decode('utf-8')


def validate_hash(password, hash_value):
    bin_pwd = password.encode('utf-8')
    bin_hash = hash_value.encode('utf-8')
    return bcrypt.checkpw(bin_pwd, bin_hash)


def register_user():
    user_name = input("Enter username: ")
    user_pwd = input("Enter password: ")

    hashed = hash_password(user_pwd)

    with open("user.txt", "a") as f:
        f.write(f"{user_name},{hashed}\n")


def login_user():
    user_name = input("Enter username: ")
    user_pwd = input("Enter password: ")

    with open("user.txt", "r") as f:
        users = f.readlines()

    for user in users:
        name, hash_value = user.strip().split(",")
        if user_name == name:
            return validate_hash(user_pwd, hash_value)

    return False








def migrating_datasets_metadata(conn):
    data = pd.read_csv('DATA/datasets_metadata.csv')
    data.to_sql('datasets_metadata', conn)

def migrating_cyber_incidents(conn):
    data = pd.read_csv('DATA/cyber_incidents.csv')
    data.to_sql('cyber_incidents', conn)

def migrating_it_tickets(conn):
    data = pd.read_csv('DATA/it_tickets.csv')
    data.to_sql('it_tickets', conn)


conn = sqlite3.connect('DATA/intelligence_platform.db')
migrating_it_tickets(conn)
conn.close()