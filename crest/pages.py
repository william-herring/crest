from abc import abstractmethod


class Page:
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
        with open(self.template, 'r') as temp:
            content = temp.read()
            for prop in self.props().keys():
                content = content.replace('{ ' + prop + ' }', self.props().get(prop))

            return content


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
        with open(self.template, 'r') as temp:
            content = temp.read()
            for prop in self.props().keys():
                content = content.replace('{ ' + prop + ' }', self.props().get(prop))

            return content


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
        with open(self.template, 'r') as temp:
            content = temp.read()
            for prop in self.props().keys():
                content = content.replace('{ ' + prop + ' }', self.props().get(prop))

            return content
