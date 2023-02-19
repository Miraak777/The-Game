from core.constants.server_constants import ServerEndpoints
from core.common import get_server_url
from flask import json
import requests

URL = get_server_url()


def get_server_resources_list() -> dict[str, list[str]]:
    data = requests.get(URL + ServerEndpoints.RESOURCES_LIST).content.decode()
    data = json.loads(data)
    return data
