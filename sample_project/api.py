from crest.api import Handler


class GetNumber(Handler):
    route = 'api/get-number'
    method = 'GET'

    def handle(self, req):
        pass
