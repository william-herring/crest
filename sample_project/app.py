from crest.app import App
from pages import *
from api import GetNumber

MyApp = App(__file__, [
    ExamplePage(),
    DynamicExamplePage(),
    QueriedExamplePage(),
], [
    GetNumber()
])

MyApp.run()
