if __name__ == '__main__':
    from paste import httpserver
    from paste.deploy import loadapp
    httpserver.serve(loadapp('config:config.ini', relative_to='.'),
                     host='10.40.96.199', port='8100')
