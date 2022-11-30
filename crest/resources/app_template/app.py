from crest.app import App
from pages import ExamplePage
from api import ExampleHandler

MyApp = App(__file__, [
    ExamplePage()
], [
    ExampleHandler()
])

MyApp.run()
