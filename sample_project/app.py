from crest.apps import App
from sample_project.pages.example import ExamplePage
from sample_project.pages.dynamic_example import DynamicExamplePage, QueriedExamplePage

MyApp = App([
    ExamplePage(),
    DynamicExamplePage(),
    QueriedExamplePage()
])

MyApp.run()
