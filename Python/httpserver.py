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

        #Declaring variables:
        ipaddr = ""
        macaddr = ""

        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        if s.path[:16] == '/registeraddress':
            #parse ip address and mac address in the form "hostname/?ipaddr=1.2.3.4&macaddr=00:00:00:00:00:00":
            allofpath = s.path.split('?')
            variablestogether = allofpath[1]
            variablesseparate = variablestogether.split('&')
            if len(variablesseparate) > 1:
                var1 = variablesseparate[0].split('=')
                if var1[0] == 'ipaddr' and len(var1) == 2:
                    ipaddr = var1[1] 
                var2 = variablesseparate[1].split('=')
                if var2[0] == 'macaddr' and len(var2) == 2:
                    macaddr = var2[1]
            s.wfile.write("ipaddr="+ipaddr+",macaddr="+macaddr)
                    
        if s.path[:14] == '/histogramdata':
                s.wfile.write("{ \"resolution\":10,")
                s.wfile.write("\"frequencies\":[0,0,0,0,3,5,5,15,9,1],")
                s.wfile.write("\"numStudents\": 38 }")
            
        if s.path == '/' or s.path == '':
                #s.wfile.write("the index.html should be printed out now")
                f = open("index.html","r")
                htmltext = f.read()
                print htmltext
                s.wfile.write(htmltext)
                s.wfile.write("<!--html-written-->")


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((server_host, server_port), RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
