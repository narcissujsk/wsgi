from wsgiref.simple_server import make_server
from paste import httpserver
from paste.deploy import loadapp
import os

if __name__ == '__main__':
    configfile = 'configure.ini'
    appname = 'main'
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)

    server = make_server('localhost', 8000, wsgi_app)
    server.serve_forever()