# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os

hostName = ""
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Very simple webapp</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        if self.path == "/hostname":
            self.wfile.write(bytes(socket.gethostname(), "utf-8"))
        elif self.path == "/author":
            self.wfile.write(bytes(os.environ["AUTHOR"], "utf-8"))
        elif self.path == "/id":
            self.wfile.write(bytes(os.environ["UUID"], "utf-8"))
        else:
            self.wfile.write(bytes("<p>Nothing found in path %s </p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")