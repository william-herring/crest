from crest.apps import App
from pages.example import ExamplePage

MyApp = App([
    ExamplePage(),
])

MyApp.run()