from crest.api import Handler, Response
import random


class GetNumber(Handler):
    route = '/get-number'
    method = 'GET'

    def handle(self, req):
        num = random.randint(0, 10)
        return Response(
            200,
            "{'Content-Type': 'text/html'}",
            str({'Number': num}),
        )
