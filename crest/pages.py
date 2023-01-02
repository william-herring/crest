from abc import abstractmethod
from crest.templates import Engine

engine = Engine()


class Page:
    """
    Base page class that stores a route and template.
    """

    @property
    @abstractmethod
    def template(self):
        pass

    @property
    @abstractmethod
    def route(self):
        pass

    def check_route(self, url):
        return url == self.route

    def render(self):
        return open(self.template, 'r').read()


class PageWithProps(Page):
    """
    Used to build pages that pass properties to a template.
    """

    @property
    @abstractmethod
    def props(self):
        pass

    def render(self):
        return engine.render(self.template, self.props())


class DynamicPage(Page):
    """
    Used to build pages with dynamic routes.
    """

    def __init__(self):
        self.query = ''

    @property
    @abstractmethod
    def props(self):
        pass

    def check_route(self, url: str):
        base = self.route.split('[')
        try:
            url.split(base[0])[1]
        except IndexError:
            return False

        self.query = url.split(base[0])[1]
        return True

    def render(self):
        return engine.render(self.template, self.props())


class QueriedPage(Page):
    """
    Used to build pages with dynamic routes.
    """

    def __init__(self):
        self.query = ''

    @property
    @abstractmethod
    def props(self):
        pass

    def check_route(self, url: str):
        base = url.split('?')
        if base[0] == self.route:
            self.query = base[1].split('=')[1]
            return True
        return False

    def render(self):
        return engine.render(self.template, self.props())
