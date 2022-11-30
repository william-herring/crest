# DynamicPage

```DynamicPage``` is used to build pages with dynamic routes. Its structure
is very similar to ```PageWithProps```, but allows the page query to be accessed
inside methods like ```props```.

## Properties

| Property       | Type         | Example                        |
|----------------|--------------|--------------------------------|
| ```route```    | ```str```    | ```route='/example/[title]'``` |
| ```template``` | ```str```    | ```path='example.html'```      |
| ```props```    | ```dict()``` | See below                      |

## Example
```python
from crest.pages.dynamic import DynamicPage


class DynamicExamplePage(DynamicPage):
    route = '/example/[title]'
    template = 'example.html'

    def props(self):
        return {
            'title': self.query,
        }

```