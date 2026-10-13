import bcrypt
from backend.database import load_users, save_users


def hash_password(password):

    encrypted_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return encrypted_password.decode()



def verify_password(password, hashed_password):

    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )



def register_user(name, email, password):

    users = load_users()

    for user in users:
        if user["email"] == email:
            return False


    new_user = {
        "name": name,
        "email": email,
        "password": hash_password(password)
    }


    users.append(new_user)

    save_users(users)

    return True



def login_user(email, password):

    users = load_users()


    for user in users:

        if user["email"] == email:

            if verify_password(
                password,
                user["password"]
            ):
                return user


    return None