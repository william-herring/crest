from crest.app import App
from pages import *

MyApp = App(__file__, [
    ExamplePage(),
    DynamicExamplePage(),
    QueriedExamplePage(),
])

MyApp.run()
