import io
from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import json


class TrxServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api":
            conn = sqlite3.connect("db/db")

            cursor = conn.cursor()
            q = "SELECT * FROM balance"
            cursor.execute(q)
            balances = json.dumps(cursor.fetchall())
            conn.close()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(str.encode(balances))
        elif self.path in ["/index.html", "/"]:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            f = open("index.html")
            self.wfile.write(str.encode(f.read()))
            f.close()
        else:
            self.send_error(404)


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Server online...")
    httpd.serve_forever()


if __name__ == "__main__":
    run(server_class=HTTPServer, handler_class=TrxServer)
