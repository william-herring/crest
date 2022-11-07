from abc import ABC, abstractmethod


class PageWithProps(ABC):
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

    def render(self):
        with open(self.template, 'r') as temp:
            content = temp.read()
            for prop in self.props().keys():
                content = content.replace('{ ' + prop + ' }', self.props().get(prop))

            return content
