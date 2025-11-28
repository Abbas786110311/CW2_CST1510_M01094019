from log_hash import register_user, login_user

def menu():
    print('*' * 30)
    print('*** Welcome to my system ***')
    print('Choose from the following options:')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    print('*' * 30)


def main():
    while True:
        menu()
        choice = input("> ")

        if choice == '1':
            register_user()
            print("User registered successfully!")

        elif choice == '2':
            if login_user():
                print("Login successful!")
            else:
                print("Login failed! Invalid username or password.")

        elif choice == '3':
            print("Goodbye!")
            break



import sqlite3

conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
)
'''
curr.execute(sql)

conn.commit()
conn.close()
