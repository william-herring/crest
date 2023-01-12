import re


class Engine:
    """
    The Crest template engine is a collection of methods for interpreting and translating template syntax.
    """

    def __init__(self):
        self.statements = {
            'consider': self.handle_conditional,
            'map': self.handle_map,
        }

    def handle_conditional(self, statement, props):
        function_in = statement.split('->')[0]
        function_out = statement.split('->')[1]
        result = ''

        condition_name = function_in.split()[1]
        if props[condition_name]:
            result = function_out.split(':')[0]
        else:
            result = function_out.split(':')[1]

        return result

    def handle_map(self, statement, props):
        function_in = statement.split('->')[0]
        function_out = statement.split('->')[1]
        result = ''

        iterator_name = function_in.split()[1]
        iterable_name = function_in.split()[3]
        for i in props[iterable_name]:
            result += function_out.replace('{' + iterator_name + '}', str(i))

        return result

    def render(self, template: str, props: dict):
        """
        Crest templates are rendered by mapping the correct values to their declarations, and then inline logic
        is interpreted and evaluated.
        """
        with open(template, 'r') as temp:
            content = temp.read()
            for prop in props.keys():
                if '{ ' + prop + ' }' in content:
                    content = content.replace('{ ' + prop + ' }', props.get(prop))
                if '{' + prop + '}' in content:
                    content = content.replace('{' + prop + '}', props.get(prop))

            logic = re.findall('(?<={%)(.*?)(?=%})', content)
            for statement in logic:
                try:
                    content = content.replace(statement, self.statements[statement.split()[0]](statement, props))
                except KeyError:
                    continue

            content = content.replace('{%', '')
            content = content.replace('%}', '')
            return content
