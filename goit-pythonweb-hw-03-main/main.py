import mimetypes
import pathlib
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

STORAGE_PATH = pathlib.Path('storage')
STORAGE_FILE = STORAGE_PATH / 'data.json'


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        env = Environment(loader=FileSystemLoader('./templates'))
        pr_url = urllib.parse.urlparse(self.path)
        current_path = pr_url.path

        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            template = env.get_template('index.html')
            content = template.render(current_path=current_path, title="Home")
            self.render_page(content)
        elif pr_url.path == '/message':
            template = env.get_template('message.html')
            content = template.render(current_path=current_path, title="Messages")
            self.render_page(content)
        elif pr_url.path == '/read':
            data = self.format_data(self.retreive_messages())
            template = env.get_template('read.html')
            content = template.render(messages=data, current_path=current_path, title="Read")
            self.render_page(content)
        else:
            static_file_path = pathlib.Path('public') / pr_url.path[1:]
            if static_file_path.exists():
                self.send_static(static_file_path)
            else:
                template = env.get_template('error.html')
                content = template.render(title="Error")
                self.render_page(content, status=404)

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}

        self.save_message(data_dict)

        self.send_response(302)
        self.send_header('Location', '/read')
        self.end_headers()

    def render_page(self, content, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def send_static(self, path):
        self.send_response(200)
        mt = mimetypes.guess_type(path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(  path, 'rb') as file:
            self.wfile.write(file.read())

    def save_message(self, message: dict):
        STORAGE_PATH.mkdir(parents=True, exist_ok=True)

        data = self.retreive_messages()

        timestamp = datetime.now().isoformat()
        data[timestamp] = message

        with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def retreive_messages(self):
        if STORAGE_FILE.exists() and STORAGE_FILE.stat().st_size > 0:
            with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        return data

    def format_data(self, data):
        formatted_data = {}
        for timestamp, message in data.items():
            formatted_timestamp = datetime.fromisoformat(timestamp).strftime('%Y-%m-%d %H:%M')
            message_copy = message.copy()
            message_copy["datetime"] = formatted_timestamp
            formatted_data[timestamp] = message_copy

        return formatted_data


def run_server():
    server = HTTPServer(('0.0.0.0', 3000), HttpHandler)
    try:
        print("Server is running at http://localhost:3000. Press CTRL+C to stop.")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nReceived shutdown signal (CTRL+C), stopping the server...")
        server.shutdown()


if __name__ == "__main__":
    run_server()
    print("Server has been stopped.")
