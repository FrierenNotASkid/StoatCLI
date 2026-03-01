import requests

from colorama import Fore

from utility.get_time import get_time

def resolve_username(user_id:str , token:str):

    """
    Fetch a users username from their ID.
    """

    URL = f"https://api.revolt.chat/users/{user_id}"

    headers = {

        "X-Session-Token": f"{token}"

    }

    response = requests.get(URL , headers = headers)
    if response.status_code == 200:
        j = response.json()
        username = j["username"]
        return username
    elif response.status_code == 401:
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"You are not authorised.")
    else:
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"A HTTP exception happened: " , response.status_code)
        return