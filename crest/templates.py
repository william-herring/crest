import re


class Engine:
    """
    The Crest template engine is a collection of methods for interpreting and translating template syntax.
    """

    def __init__(self):
        self.statements = {
            'if': self.handle_if,
            'for': self.handle_for,
        }

    def handle_if(self, statement):
        print(statement)

    def handle_for(self, statement):
        print(statement)

    def render(self, template: str, props: dict):
        """
        Crest templates are rendered by mapping the correct values to their declarations, and then inline logic
        is interpreted and evaluated.
        """
        with open(template, 'r') as temp:
            content = temp.read()
            for prop in props.keys():
                content = content.replace('{ ' + prop + ' }', props.get(prop))

            logic = re.findall('(?<={%)(.*?)(?=%})', content)
            for statement in logic:
                try:
                    self.statements[statement.split()[0]](statement)
                except KeyError:
                    continue

            return content
