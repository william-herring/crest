# PageWithProps

```PageWithProps``` is used to build pages that pass properties to a template.

## Properties

| Property       | Type         | Example                     |
|----------------|--------------|-----------------------------|
| ```route```    | ```str```    | ```route='/example'```      |
| ```template``` | ```str```    | ```path='example.html'```   |
| ```props```    | ```dict()``` | See below                   |

## Example
```python
from crest.pages import PageWithProps
import datetime


class ExamplePage(PageWithProps):
    route = '/example'
    template = 'example.html'

    def props(self):
        return {
            'message': f'The time is {datetime.datetime.now()}',
            'lipsum': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae velit tincidunt eros sagittis blandit.'
        }
```