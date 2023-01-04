import re


class Engine:
    """
    The Crest template engine is a collection of methods for interpreting and translating template syntax.
    """

    def __init__(self):
        self.statements = {
            'if': self.handle_if,
            'map': self.handle_map,
        }

    def handle_if(self, statement, props):
        print(statement)

    def handle_map(self, statement, props):
        print(f'Statement to execute: {statement}')
        function_in = statement.split('->')[0]
        function_out = statement.split('->')[1]
        result = ''

        iterator_name = function_in.split()[1]
        iterable_name = function_in.split()[3]
        for i in props[iterable_name]:
            result += function_out.replace('{' + iterator_name + '}', str(i))
            print(i)

        print(result)
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

            logic = re.findall('(?<={%)(.*?)(?=%})', content)
            for statement in logic:
                try:
                    content = content.replace(statement, self.statements[statement.split()[0]](statement, props))
                except KeyError:
                    continue

            content = content.replace('{%', '')
            content = content.replace('%}', '')
            return content
