from http.server import HTTPServer, BaseHTTPRequestHandler

from socketserver import ThreadingMixIn

import requests

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "http://python.vic-tim.de/images/cat.jpg":
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg")
            self.end_headers()

            with open("./cats/1.jpg", "rb") as file:
                self.wfile.write(file.read())
                
        else:
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