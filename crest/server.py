import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import importlib.resources as pkg_resources
from crest.resources.error_pages import templates
from crest.api import Request
from crest.templates import Engine


host = 'localhost'
engine = Engine()
error_html = {
    '404': pkg_resources.read_text(templates, '404.html'),
    'error': pkg_resources.read_text(templates, 'error.html')
}

_pages = []
_handlers = []
_entrypoint = '/'


class DevServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.handle_API('GET'):
            return
        if self.path == '/' and _entrypoint != '/':
            print(_entrypoint)
            self.send_response(307)
            self.send_header('Location', _entrypoint)
            self.end_headers()

        for page in _pages:
            if page.check_route(self.path):
                try:
                    rendered = page.render()
                    self.send_response(200)
                except Exception as e:
                    rendered = engine.render(__file__.split('server.py')[0] + 'resources/error_pages/templates/error.html', {
                        'error_msg': str(e)
                    })
                    self.send_response(500)

                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(rendered, 'utf-8'))
                return

        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(error_html['404'], 'utf-8'))

    def handle_API(self, method):
        if self.path.startswith('/api/'):
            content_length = 0
            if 'Content-Length' in self.headers:
                content_length = int(self.headers.get('Content-Length'))
            req = Request(
                self.requestline,
                self.headers,
                self.rfile.read(content_length)
            )
            for handler in _handlers:
                if handler.route == self.path.split('/api')[1] and handler.method == method:
                    data = handler.handle(req)
                    self.send_response(data.status)
                    for header in data.headers.keys():
                        self.send_header(header, data.headers[header])
                    self.end_headers()
                    self.wfile.write(bytes(data.body, 'utf-8'))
                    return True
        return False


def start(app, pages, handlers, port=8000, entrypoint='/'):
    global _pages
    global _entrypoint
    global _handlers
    _pages = pages
    _entrypoint = entrypoint
    if handlers is not None:
        _handlers = handlers
    server = HTTPServer((host, port), DevServer)

    app_templates = os.listdir(app.root + 'templates/')
    for k in error_html.keys():
        if f'_{k}.html' in app_templates:
            error_html[k] = open(app.root + 'templates/' + f'_{k}.html', 'r').read()

    print(f'Server started at http://{host}:{port}. Ready to accept connections.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server no longer accepting connections.')