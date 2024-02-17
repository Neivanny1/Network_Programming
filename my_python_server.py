#!/usr/bin/python3
"""
Importing modules
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

port = 8000
host = '127.0.0.1'

class MyServer(BaseHTTPRequestHandler):
    '''
    Get request handling
    '''
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<h1>HELLO ERICk</h1>', 'utf-8'))


server = HTTPServer((host, port), MyServer)
print(f'Starting server on {host}:{port}')
server.serve_forever()
