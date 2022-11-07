from http.server import BaseHTTPRequestHandler, HTTPServer

host = 'localhost'
placeholder_html = "<html><head><title>Crest</title></head><body><h1>Crest is running!</h1><br><p>Read " \
                   "the docs.</p></body></html> "

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
            new_page = page()
            if new_page.route in self.path:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(new_page.render(), 'utf-8'))
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
