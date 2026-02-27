import requests

from colorama import Fore

from utility.get_time import get_time

def login_user(email:str , password:str) -> str:

    """
    Log in a user to Stoat and obtain the token.
    """

    URL = "https://api.revolt.chat/auth/session/login"

    headers = {

        "Content-Type": "application/json"

    }
    payload = {

        "email" : f"{email}",
        "password" : f"{password}",
        "friendly_name" : None

    }

    response = requests.post(URL , json = payload , headers = headers)
    if response.status_code == 200:
        j = response.json()
        token = j["token"]
        with open(".auth" , "w") as auth_file:
            auth_file.write(token)
        return token
    elif response.status_code == 401:
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"Either your email or password was incorrect. Please retry or make an account")
        return
    else:
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"A HTTP exception happened:" , response.status_code)
        return