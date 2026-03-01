import json
import websockets

from colorama import Fore

from servers.get_servers import fetch_servers
from session.event_handler import handle_event
from utility.get_time import get_time

async def listen(websocket_url):

    """
    Listen for events
    """

    async with websockets.connect(websocket_url) as ws:
        async for raw in ws:
            try:
                event = json.loads(raw)
                if isinstance(event , dict) and "servers" in event:
                    fetch_servers(raw)
                await handle_event(event)
            except json.JSONDecodeError:
                print(Fore.MAGENTA + f"[ {get_time()} ]" , Fore.RED + f"An error happened whilst parting the raw websocket data: " , raw)