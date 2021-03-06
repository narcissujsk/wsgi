# tap.py
class Tap(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Tap')
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s, %s!\n' % (self.in_arg, 'Tap')]


def app_factory(global_config, in_arg):
    return Tap(in_arg)