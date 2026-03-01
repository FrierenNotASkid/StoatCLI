import asyncio
import configparser
import os

from colorama import Fore

from auth.auth_exists import *
from auth.login import login_user
from channels.select_channels import select_channel
from session.websocket_listener import listen
from utility.get_time import get_time

async def user_input(token):

    """
    This function was named by .xdcraze16 on Discord.
    """

    current_channel = None

    while True: ## Message loop
        
        if current_channel == None:
            current_channel = select_channel(token)

async def main():

    """
    The entry point for StoatCLI.
    """

    os.system("cls")
    os.system("title StoatCLI")

    present = is_token_present()
    if present == False:
        while True:
            email = input(Fore.MAGENTA + f"[ {get_time()} ] " + Fore.WHITE + "Enter your email: ")
            password = input(Fore.MAGENTA + f"[ {get_time()} ] " + Fore.WHITE + "Enter your password: ")
            token = login_user(email , password)
            if token != None:
                os.system("cls")
                break
            else:
                continue
    else:
        token = extract_token()

    config = configparser.ConfigParser()
    config.read(".config")

    websocket_url_partial = config["websocket"]["websocket_url"]
    websocket_url = websocket_url_partial + token

    await asyncio.gather(
        listen(websocket_url),
        user_input(token)
    )

asyncio.run(main())