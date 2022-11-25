# QueriedPage

```QueriedPage``` is used to build pages with dynamic routes.

## Properties

| Property       | Type         | Example                             |
|----------------|--------------|-------------------------------------|
| ```route```    | ```str```    | ```route='/example'```              |
| ```template``` | ```str```    | ```path='templates/example.html'``` |
| ```props```    | ```dict()``` | See below                           |

## Example
```python
from crest.pages.dynamic import QueriedPage


 # Try going to /example?title=example to see how queried pages work
class QueriedExamplePage(QueriedPage):
    route = '/example'
    template = 'templates/example.html'

    def props(self):
        return {
            'title': self.query,
        }

```