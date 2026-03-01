import requests
import json

from colorama import Fore

from utility.get_time import get_time

def select_channel(token):

    """
    Select a channel 
    """

    with open("config.json") as config_file:
        config = json.load(config_file)

    headers = {

        "X-Session-Token" : f"{token}"

    }

    for index , server in enumerate(config["servers"]):
        URL = "https://api.revolt.chat/servers/" + server
        response = requests.get(URL , headers = headers)
        if response.status_code == 200:
            j = response.json()
            for channel in j["channels"]:
                pass
        elif response.status_code == 401:
            print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"Either your email or password was incorrect. Please retry or make an account")
            return
        else:
            print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"A HTTP exception happened:" , response.status_code)
            return