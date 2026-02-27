import json
import websockets

from session.event_handler import handle_event

async def listen(websocket_url):

    """
    Listen for events
    """

    async with websockets.connect(websocket_url) as ws:
        async for raw in ws:
            try:
                event = json.loads(raw)
                await handle_event(event)
            except json.JSONDecodeError:
                print("[Error] Failed to parse event:", raw)