from crest.pages import PageWithProps
import datetime


class ExamplePage(PageWithProps):
    # Need to find some way to shorten this
    route = '/example'
    template = '/Users/williamherring/Development/crest/sample_project/pages/templates/example.html'

    def props(self):
        return {
            'message': f'The time is {datetime.datetime.now()}',
            'lipsum': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae velit tincidunt eros sagittis blandit.'
        }
