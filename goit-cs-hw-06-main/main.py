from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import urllib.parse
import os
import mimetypes

PORT = 3000
SOCKET_HOST = 'socket'
SOCKET_PORT = 5000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/': 'templates/index.html',
            '/message.html': 'templates/message.html',
        }

        if self.path.startswith('/static/'):
            return self.serve_static(self.path)

        file_path = routes.get(self.path, 'templates/error.html')
        self.send_response(200 if file_path in routes.values() else 404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open(file_path, 'rb') as f:
            self.wfile.write(f.read())

    def serve_static(self, path):
        file_path = path.lstrip('/')
        if not os.path.isfile(file_path):
            self.send_error(404, 'Static file not found')
            return

        mime_type, _ = mimetypes.guess_type(file_path)
        self.send_response(200)
        self.send_header('Content-type', mime_type or 'application/octet-stream')
        self.end_headers()

        with open(file_path, 'rb') as f:
            self.wfile.write(f.read())

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode())

            username = data.get('username', [''])[0]
            message = data.get('message', [''])[0]

            msg = f"username={username}&message={message}"

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((SOCKET_HOST, SOCKET_PORT))
                    s.sendall(msg.encode())
            except Exception as e:
                print("Socket send failed:", e)

            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', PORT), SimpleHandler)
    print(f"HTTP Server running on http://localhost:{PORT}")
    server.serve_forever()
