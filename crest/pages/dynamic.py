from abc import ABC, abstractmethod


class DynamicPage(ABC):
    def __init__(self):
        self.query = ''

    @property
    @abstractmethod
    def template(self):
        pass

    @property
    @abstractmethod
    def props(self):
        pass

    @property
    @abstractmethod
    def route(self):
        pass

    # Must call before render
    def check_route(self, url: str):
        base = self.route.split('[')
        try:
            url.split(base[0])[1]
        except IndexError:
            return False

        self.query = url.split(base[0])[1]
        return True

    def render(self):
        with open(self.template, 'r') as temp:
            content = temp.read()
            for prop in self.props().keys():
                content = content.replace('{ ' + prop + ' }', self.props().get(prop))

            return content
