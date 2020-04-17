# coding=utf-8
import sys
def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [f'Request {environ["REQUEST_METHOD"]} {environ["PATH_INFO"]} has been processed\r\n'.encode('utf-8')]