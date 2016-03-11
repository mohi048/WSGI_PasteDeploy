class MyApp1:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s %s!\n' % (self.name, self.greeting)]

def my_func1(global_config, t1='DEFAULT', t2='TEXT'):
    return MyApp1('Hello','World')

