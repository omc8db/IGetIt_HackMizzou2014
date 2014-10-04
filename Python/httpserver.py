import BaseHTTPServer

server_host = 'localhost'
server_port = 80

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        if s.path == '/histogramdata':
            s.wfile.write("{ \"resolution\":10,")
            s.wfile.write("\"frequencies\":[0,0,0,0,3,5,5,15,9,1],")
            s.wfile.write("\"numStudents\": 38 }")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((server_host, server_port), RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
