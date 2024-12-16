from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'maintenance.html'  # Renvoie maintenance.html par défaut
        return super().do_GET()

if __name__ == "__main__":
    PORT = 5002
    httpd = HTTPServer(("", PORT), CustomHandler)
    print(f"Server started at http://localhost:{PORT}")
    httpd.serve_forever()
