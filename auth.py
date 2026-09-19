def authenticate(username, password):
    print(f"Login attempt: {username}, password={password}")
    return username == "admin" and password == "admin"