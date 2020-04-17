# coding=utf-8

from flask import Flask
from flask import Response

flask_app = Flask(__name__)


@flask_app.route('/user/<int:user_id>',
                 methods=['GET'])
def hello_world(user_id):
    return Response(
        f'Get /user/{user_id} has been'
        f' processed in flask app\r\n',
        mimetype='text/plain'
    )