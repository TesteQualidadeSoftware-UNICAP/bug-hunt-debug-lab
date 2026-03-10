def email_valido(email):

    # BUG: validação muito simplista
    if "@" in email:
        return True

    return False
