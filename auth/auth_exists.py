def is_token_present() -> bool:

    """
    Check if a token is present in .auth and try to log in with it.
    """

    try:
        with open(".auth" , "r") as auth_file:
            lines = auth_file.readlines()
            token = lines[0]
        if token != None:
            return True
    except IndexError:
        return False
    
def extract_token() -> str:

    """
    Return the token.
    """

    with open(".auth" , "r") as auth_file:
        lines = auth_file.readlines()
        token = lines[0]
    
    return token