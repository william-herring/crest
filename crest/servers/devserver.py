from http.server import BaseHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8000
placeholder_html = "<html><head><title>Crest</title></head><body><h1>Crest is running!</h1><br><p>Read " \
                   "the docs.</p></body></html> "


class DevServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(placeholder_html, 'utf-8'))


def start():
    server = HTTPServer((host, port), DevServer)
    print(f'Server started at http://{host}:{port}. Ready to accept connections.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server no longer accepting connections.')