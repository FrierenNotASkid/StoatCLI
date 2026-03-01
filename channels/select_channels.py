import requests
import json

from colorama import Fore

from channels.resolve_channel import resolve_channel_name
from servers.resolve_server import resolve_server_name
from utility.get_time import get_time

def select_channel(token) -> str:

    """
    Select a channel
    """

    with open("config.json") as config_file:
        config = json.load(config_file)

    headers = {

        "X-Session-Token" : f"{token}"

    }

    for s_index , server in enumerate(config["servers"]):
        URL = "https://api.revolt.chat/servers/" + server
        response = requests.get(URL , headers = headers)
        server_name = resolve_server_name(server , token)
        if response.status_code == 200:
            j = response.json()
            for c_index , channel in enumerate(j["channels"]):
                channel_name = resolve_channel_name(channel)
                print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.WHITE + f"[ {s_index} : {c_index} ] [ {server_name} ] [ {channel_name} ]")
        elif response.status_code == 401:
            print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"Either your email or password was incorrect. Please retry or make an account")
            return
        else:
            print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"A HTTP exception happened:" , response.status_code)
            return
    
    while True:
        selected_server = input(Fore.MAGENTA + f"[ {get_time()} ] " + Fore.WHITE + f"Please select a server number: ")
        if type(selected_server) != int:
            print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"The selected server number must be an integer")
            continue
        else:
            if selected_server < 0 or selected_server > len(config["servers"]):
                print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"The selected server is out of range. Please try again")
                continue
            else:
                pass
        selected_channel = input(Fore.MAGENTA + f"[ {get_time()} ] " + Fore.WHITE + f"Please select a channel number: ")
        if type(selected_channel) != int:
            print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"The selected server number must be an integer")
            continue
        else:
            URL = "https://api.revolt.chat/servers/" + server
            response = requests.get(URL , headers = headers)
            if response.status_code == 200:
                j = response.json()
                if selected_channel < 0 or selected_channel > len(j["channels"]):
                    print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"The selected server is out of range. Please try again")
                    continue
                else:
                    return j["channels"][selected_channel]
            elif response.status_code == 401:
                print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"Either your email or password was incorrect. Please retry or make an account")
                return
            else:
                print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"A HTTP exception happened:" , response.status_code)
                return