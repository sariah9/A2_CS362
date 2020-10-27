def check_pwd(password):
    if 8 <= len(password) <= 20:
        return True
    return False

