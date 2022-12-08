class Engine:
    """
    The Crest template engine is a collection of methods for interpreting and translating template syntax.
    """
    def __init__(self):
        self.statements = {
            'if': self.handle_if,
            'for': self.handle_for,
        }

    def handle_if(self, read_template, start_from):
        pass

    def handle_for(self, read_template, start_from):
        pass

    def render(self, template: str, props: dict):
        """
        Crest templates are rendered by mapping the correct values to their declarations, and then inline logic
        is interpreted and evaluated.
        """
        with open(template, 'r') as temp:
            content = temp.read()
            for prop in props.keys():
                content = content.replace('{ ' + prop + ' }', props.get(prop))

            return content
