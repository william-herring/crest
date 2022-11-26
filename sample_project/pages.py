from crest.pages import DynamicPage, QueriedPage, PageWithProps
import datetime


class DynamicExamplePage(DynamicPage):
    route = '/dyn/[title]'
    template = 'dynamic.html'

    def props(self):
        return {
            'title': self.query,
        }


class QueriedExamplePage(QueriedPage):
    route = '/queried'
    template = 'dynamic.html'

    def props(self):
        return {
            'title': self.query,
        }


class ExamplePage(PageWithProps):
    route = '/example'
    template = 'example.html'

    def props(self):
        return {
            'message': f'The time is {datetime.datetime.now()}',
            'lipsum': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae velit tincidunt eros sagittis blandit.'
        }
