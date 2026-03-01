from colorama import Fore

from auth.auth_exists import extract_token
from utility.get_time import get_time
from users.resolve_user import resolve_username

async def handle_event(event: dict):

    """
    Handle incoming websocket events.
    """

    event_type = event.get("type")
    if event_type == "Ready":
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.GREEN + f"[ SYSTEM ] Connection ready: Initial state recieved.")
    elif event_type == "Message":
        print(event)
        token = extract_token()
        author_id = event.get("author")
        author_username = resolve_username(author_id , token)
        content = event.get("content")
        print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.CYAN + f"[ {author_username} ]" , Fore.WHITE + f"{content}")
    elif event_type == "MessageUpdate":
        pass
    elif event_type == "MessageDelete":
        pass
    elif event_type == "Pong":
        pass
    else:
        pass