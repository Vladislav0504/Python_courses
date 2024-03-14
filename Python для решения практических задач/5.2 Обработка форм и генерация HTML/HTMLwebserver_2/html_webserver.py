"""HTML webserver."""
from http.server import HTTPServer, CGIHTTPRequestHandler


def main():
    """My function."""
    number = 8002
    server_address = ("", number)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
