from http.server import BaseHTTPRequestHandler, HTTPServer
import importlib.resources as pkg_resources
from crest import resources

host = 'localhost'
placeholder_html = pkg_resources.read_text(resources, 'placeholder.html')

_pages = []
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


def start(pages, port=8000, entrypoint='/'):
    global _pages
    global _entrypoint
    _pages = pages
    _entrypoint = entrypoint
    server = HTTPServer((host, port), DevServer)
    print(f'Server started at http://{host}:{port}. Ready to accept connections.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server no longer accepting connections.')
