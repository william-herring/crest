# Understanding Project Structure

When you create a Crest app, your file structure will look something like this:
```
myapp
|   api.py
│   app.py    
│   pages.py
│   README.md
|
└───templates
    │   sample.html
```
The most simple concepts you must understand are Apps, Pages and Templates. 

## Apps
Your application is run from the ```app.py``` file. 
This file is generated with a basic app component, which will contain all your pages, API handlers and runtime configurations. It will look like this:

```python
from crest.app import App
from pages import SamplePage
from api import SampleHandler

MyApp = App(__file__, [
    SamplePage()
], [
    SampleHandler()
])

MyApp.run()
```
The App component specifies what is contained inside the app. This includes pages and configurations. For example, you may pass an entrypoint
argument, which will redirect the '/' route to something else.
```python
MyApp = App(__file__, [
    SamplePage()
], [
    SampleHandler()
] entrypoint='/sample')
```

In most cases, the basic App component provided will work fine. However, if you wish to expand this component, you could use an inheritance-based approach
to create a custom component.
```python
class MyApp(App):
    def myfunc(self):
        # ...
        pass

    def run(self, **kwargs):
        self.myfunc()
        super().run(**kwargs)
        pass


MyApp(__file__, [
    SamplePage()
], [
    SampleHandler()
]).run()
```
The ```run()``` method begins the server and app process. You may specify a port by passing the keyword argument ```port```.

## Templates
A Template is an HTML file which defines the layout of a page. Just like you would normally do, you can import stylesheets and write client-side 
JavaScript to add functionality to Templates. Basically, you include all static content as you usually would. However, you may include variables
in a Template, which will be replaced with a value generated server-side. By doing this, non-static data can be rendered directly onto the template
at runtime. Variables are declared inside curly braces, with a space to either side of the variable name. For example, ```{ variable }```.
Here is a sample template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample</title>
</head>
<body>
    <h1>Sample page</h1>
    <p>{ content }</p>
</body>
</html>
```
A template does not necessarily have to correspond to one Page. For example, you might create a blog post template that can be used for many dynamically generated Pages.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blog | { title }</title>
</head>
<body>
    <h1>{ title }</h1>
    <h2>By { author }</h2>
    <p>{ content }</p>
</body>
</html>
```

## Pages
A Page contains the Template, route and configurations for a page. When declaring a page, you will choose between different page types. The basic types include
```PageWithoutProps```, ```PageWithProps```, ```DynamicPage``` and ```QueriedPage```. For a page which passes properties to a template, use ```PageWithProps```.
```python
from crest.pages import PageWithProps


class SamplePage(PageWithProps):
    route = '/sample'
    template = '[path_to_template]'

    def props(self):
        return {
            'content': 'Hello World'
        }

```