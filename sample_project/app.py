from crest.app import App
from sample_project.pages.example import ExamplePage
from sample_project.pages.dynamic_example import DynamicExamplePage, QueriedExamplePage

MyApp = App(__file__, [
    ExamplePage(),
    DynamicExamplePage(),
    QueriedExamplePage()
])

MyApp.run()
