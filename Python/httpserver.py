import BaseHTTPServer
import dbClient

server_host = 'localhost'
server_port = 80

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    db = dbClient.db_Connect(1)

    def __init__(self,request,client_address,server):
        print("RequestHandler constructor initialized")
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self,request,client_address,server)

    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s,i=db):
        #print("HTTP Request Recieved")
        print("path="+s.path)
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
                studname = "STUDENT"
                i.addDevice(macaddr,ipaddr,studname)
            s.wfile.write("ipaddr="+ipaddr+",macaddr="+macaddr)

        if s.path[:14] == "/histogramdata":

                #get list of latest ratings
                maxtime = i.get_max_time()
                #print("max time = "+maxtime)
                """
                studentratings = i.get_time_ratings(maxtime[1][0])
                numstudents = len(studentratings)

                #set number of bars on graph
                resolution = 10

                frequencylist = []

                #tally up frequency
                increment = numstudents/resolution

                for currentrating in studentratings:
                    lownum = 0
                    i = 0;
                    while i < resolution:
                        highnum = lownum + increment
                        if currentrating <= highnum and currentrating > lownum:
                            frequencylist[i] += 1
                        i += 1
                        lownum = highnum



                s.wfile.write("{ \"resolution\":"+resolution+",")
                s.wfile.write("\"frequencies\":"+frequencylist+",")
                s.wfile.write("\"numStudents\":"+numstudents+" }")

                """

                s.wfile.write("{ \"resolution\":10,")
                s.wfile.write("\"frequencies\":[0,0,0,3,5,5,10,15,20,10],")
                s.wfile.write("\"numStudents\":68 }")

        if s.path == '/' or s.path == '':
                #s.wfile.write("the index.html should be printed out now")
                f = open("index.html","r")
                htmltext = f.read()
                print(htmltext)
                s.wfile.write(htmltext)
                s.wfile.write("<!--html-written-->")


if __name__ == '__main__':
    print("Web Server Started")
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((server_host, server_port), RequestHandler)
    print("httpd initialized")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("server closed")
