from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        res = requests.get(self.path)
        self.send_response(res.status_code)
        for key, value in res.headers.items():
            self.send_header(key, value)
        self.end_headers()

        self.wfile.write("Hallo Welt".encode())

address = ("127.0.0.1", 10080)

server = HTTPServer(address, MyRequestHandler)
server.serve_forever()