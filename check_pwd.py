def check_pwd(password):
    if 8 <= len(password) <= 20:
        # has lowercase return True
        if password.isupper():
            return False
        return True
    return False

