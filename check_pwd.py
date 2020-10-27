def check_pwd(password):
    if 8 <= len(password) <= 20:
        # has lowercase return True
        if password.isupper():
            return False
        # has uppercase return True
        if password.islower():
            return False
        # has digit
        no_digit = True
        for character in password:
            if character.isdigit():
                no_digit = False
        if no_digit:
            return False
        # has symbol
        no_symbol = True
        symbols = ["~", "`", "!", "@", "#",
                   "$", "%", "^", "&", "*",
                   "(", ")", "_", "+", "-", "="]
        for idx in range(0, 15):
            val = symbols[idx]
            for ch in password:
                if ch == val:
                    no_symbol = False
        if no_symbol:
            return False
        return True
    return False

