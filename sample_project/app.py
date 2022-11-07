from crest.apps import App
from sample_project.pages.example import ExamplePage

MyApp = App([
    ExamplePage
], entrypoint='/example')

MyApp.run()
