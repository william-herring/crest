from crest.pages.dynamic import DynamicPage


class DynamicExamplePage(DynamicPage):
    route = '/dyn/[title]'
    template = '/Users/williamherring/Development/crest/sample_project/pages/templates/dynamic.html'

    def props(self):
        return {
            'title': self.request,
        }
