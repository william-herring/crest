from crest import server


class App:
    """
    The standard app class includes all pages and configurations required at runtime
    """
    def __init__(self, path, pages, **kwargs):
        self.path = path
        self.pages = pages
        if 'entrypoint' in kwargs:
            self.entrypoint = kwargs.get('entrypoint')
        else:
            self.entrypoint = '/'

    def run(self, **kwargs):
        """
        Starts the server at specified port (8000 if unspecified)
        """
        if 'port' in kwargs:
            server.start(self.pages, kwargs.get('port'), self.entrypoint)

        server.start(self.pages, 8000, self.entrypoint)
