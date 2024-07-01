def alphanumeric(password):
    if isinstance(password, str) and password.isalnum():
        return True
    return False