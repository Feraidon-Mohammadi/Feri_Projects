from http.server import HTTPServer, BaseHTTPRequestHandler

from socketserver import ThreadingMixIn

import requests

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        with requests.get(self.path, stream=True) as res:
            self.send_response(res.status_code)
            for key, value in res.headers.items():
                self.send_header(key, value)
            self.end_headers()

            self.wfile.write(res.raw.read())

address = ("127.0.0.1", 10080)

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

server = ThreadingHTTPServer(address, MyRequestHandler)
server.serve_forever()