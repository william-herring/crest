from crest.pages import PageWithProps, Page
import datetime


class PlaceholderPage(Page):
    route = '/'
    template = 'placeholder.html'


class ExamplePage(PageWithProps):
    route = '/example'
    template = 'example.html'

    def props(self):
        return {
            'message': f'The time is {datetime.datetime.now()}',
            'lipsum': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae velit tincidunt eros sagittis blandit.'
        }