import BaseHTTPServer
import dbClient

server_host = 'localhost'
server_port = 80

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def __init__(self):
<<<<<<< HEAD
        print "RequestHandler constructor initialized"
        self.db = db_Connect(1)
=======
        self.db = dbClient.db_Connect(1)
>>>>>>> 5945a4462556bef3c920adcf0300b0eace6e7219
        super(RequestHandler,self).__init__();

    def do_HEAD(self,s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(self,s):
        print("HTTP Request Recieved")
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
                self.db.addDevice(macaddr,ipaddr,studname)
            s.wfile.write("ipaddr="+ipaddr+",macaddr="+macaddr)
                    
        if s.path[:14] == "/histogramdata":

                #get list of latest ratings
                maxtime = self.db.get_max_time()
                studentratings = self.db.get_time_ratings(maxtime)
                ratingslist = studentratings.split("\n")[1:]
                numstudents = len(ratingslist)

                #set number of bars on graph
                resolution = 10

                frequencylist = []

                #tally up frequency
                increment = numstudents/resolution

                for currentrating in ratingslist:
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

            
        if s.path == '/' or s.path == '':
                #s.wfile.write("the index.html should be printed out now")
                f = open("index.html","r")
                htmltext = f.read()
                print htmltext
                s.wfile.write(htmltext)
                s.wfile.write("<!--html-written-->")


if __name__ == '__main__':
    print "Web Server Started"
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((server_host, server_port), RequestHandler)
    print "httpd initialized"
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print "server closed"
