# Page

```Page``` is the base page class that stores a route and template.

## Properties

| Property       | Type         | Example                     |
|----------------|--------------|-----------------------------|
| ```route```    | ```str```    | ```route='/example'```      |
| ```template``` | ```str```    | ```path='example.html'```   |

## Example
```python
from crest.pages import Page

class ExamplePage(Page):
    route = '/example'
    template = 'example.html'
```