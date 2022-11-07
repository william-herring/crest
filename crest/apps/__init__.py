from crest.servers import devserver


class App:
    def __init__(self, pages, **kwargs):
        self.pages = pages
        if 'entrypoint' in kwargs:
            self.entrypoint = kwargs.get('entrypoint')
        else:
            self.entrypoint = '/'

    def run(self, **kwargs):
        if 'port' in kwargs:
            devserver.start(self.pages, kwargs.get('port'), self.entrypoint)

        devserver.start(self.pages, 8000, self.entrypoint)
