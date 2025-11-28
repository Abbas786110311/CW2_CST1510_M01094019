import bcrypt

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
