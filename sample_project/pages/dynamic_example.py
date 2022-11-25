from crest.pages import DynamicPage, QueriedPage


class DynamicExamplePage(DynamicPage):
    route = '/dyn/[title]'
    template = '/Users/williamherring/Development/crest/sample_project/pages/templates/dynamic.html'

    def props(self):
        return {
            'title': self.query,
        }


class QueriedExamplePage(QueriedPage):
    route = '/queried'
    template = '/Users/williamherring/Development/crest/sample_project/pages/templates/dynamic.html'

    def props(self):
        return {
            'title': self.query,
        }
