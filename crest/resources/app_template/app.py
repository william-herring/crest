from crest.app import App
from pages.example import ExamplePage

MyApp = App([
    ExamplePage(),
])

MyApp.run()