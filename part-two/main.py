from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
server_port = 8080


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>My Basic WebSite</title></head>", "utf-8")
        )
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is just a Basic Website.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), Server)

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()