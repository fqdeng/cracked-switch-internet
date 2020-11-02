from flask import Flask
from flask import Response
app = Flask(__name__)
import os

@app.route('/')
def ok():
    print('ok')
    os.system('echo ok > /tmp/ok ')
    response = Response('ok\n',mimetype="text/plain")
    response.headers['X-Organization'] = 'Nintendo'
    return response
