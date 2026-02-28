import requests
import json

def fetch_servers(raw_data):

    """
    Fetch all servers on every message event.
    """

    with open("config.json" , "r") as state_file:
        j = json.load(state_file)

    server_list = j["servers"]
    servers_to_remove = []

    for server in raw_data["servers"]:
        if server in server_list:
            servers_to_remove.append(server)
        else:
            j["servers"].append(server)

    for c in servers_to_remove:
        j["servers"].remove(c)

    with open("config.json" , "w") as state_file:
        json.dump(j , state_file , indent = 4)