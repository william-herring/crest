from http.server import BaseHTTPRequestHandler, HTTPServer
import importlib.resources as pkg_resources
from crest import resources
from crest.api import Request

host = 'localhost'
placeholder_html = pkg_resources.read_text(resources, 'placeholder.html')

_pages = []
_handlers = []
_entrypoint = '/'


class DevServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' and _entrypoint != '/':
            print(_entrypoint)
            self.send_response(307)
            self.send_header('Location', _entrypoint)
            self.end_headers()

        for page in _pages:
            if page.check_route(self.path):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(page.render(), 'utf-8'))
                return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(placeholder_html, 'utf-8'))

    def handle_API(self, method):
        if self.path.startswith('/api/'):
            content_length = int(self.headers.get('Content-Length'))
            req = Request(
                self.requestline,
                self.headers,
                self.rfile.read(content_length)
            )
            # TODO: Find relevant API handler (may require some object sorting)
        return


def start(pages, handlers, port=8000, entrypoint='/'):
    global _pages
    global _entrypoint
    global _handlers
    _pages = pages
    _entrypoint = entrypoint
    if handlers is not None:
        _handlers = handlers
    server = HTTPServer((host, port), DevServer)
    print(f'Server started at http://{host}:{port}. Ready to accept connections.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server no longer accepting connections.')
