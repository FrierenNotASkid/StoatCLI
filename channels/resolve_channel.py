import requests

from colorama import Fore

from utility.get_time import get_time

def resolve_channel_name(channel_id:str , token):

    """
    Resolve a channels name.
    """

    headers = {

        "X-Session-Token" : f"{token}"

    }

    URL = "https://api.revolt.chat/channels/" + channel_id

    response = requests.post(URL , headers = headers)
    if response.status_code == 200:
        j = response.json()
        name = j["name"]
        return name
    elif response.status_code == 401:
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"You are not authorised.")
        return
    else:
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"A HTTP exception happened:" , response.status_code)
        return