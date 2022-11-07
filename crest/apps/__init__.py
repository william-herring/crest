from servers import devserver


class App:
    def __init__(self, pages, **kwargs):
        self.pages = pages
        if 'entrypoint' in kwargs:
            self.entrypoint = kwargs.get('entrypoint')
        else:
            self.entrypoint = '/'

    def render(self):
        pass

    def run(self, **kwargs):
        self.render()
        if 'port' in kwargs:
            devserver.start(kwargs.get('port'))
        devserver.start()
