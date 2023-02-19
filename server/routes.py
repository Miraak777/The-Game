from .common import get_app, get_resources_list
from flask import Response, json
from http import HTTPStatus
from .constants import ServerConstants

app = get_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/resources_list')
def resources_list() -> Response:
    data = get_resources_list()
    response = app.response_class(response=json.dumps(data), status=HTTPStatus.OK)
    return response
