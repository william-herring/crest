from crest import server


class App:
    """
    The standard app class includes all pages and configurations required at runtime
    """
    def __init__(self, path, pages, handlers=None, **kwargs):
        self.root = path.split('app.py')[0]
        self.pages = pages
        self.handlers = handlers
        if 'entrypoint' in kwargs:
            self.entrypoint = kwargs.get('entrypoint')
        else:
            self.entrypoint = '/'

    def run(self, **kwargs):
        """
        Starts the server at specified port (8000 if unspecified)
        """
        for page in self.pages:
            page.template = self.root + 'templates/' + page.template
        if 'port' in kwargs:
            server.start(self, self.pages, self.handlers, kwargs.get('port'), self.entrypoint)

        server.start(self, self.pages, self.handlers, 8000, self.entrypoint)
