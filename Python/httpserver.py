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
        ipAddr = ""
        macAddr = ""

        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        if s.path[:16] == '/registeraddress':
            #parse ip address and mac address in the form "hostname/?ipaddr=1.2.3.4&macAddr=00:00:00:00:00:00":
            pathSplit = s.path.split('?')
            pathVariables = pathSplit[1]
            variablesSeparate = pathVariables.split('&')
            if len(variablesSeparate) > 1:
                var1 = variablesSeparate[0].split('=')
                if var1[0] == 'ipaddr' and len(var1) == 2:
                    ipAddr = var1[1]
                var2 = variablesSeparate[1].split('=')
                if var2[0] == 'macAddr' and len(var2) == 2:
                    macAddr = var2[1]
                studName = "STUDENT"
                i.addDevice(macAddr,ipAddr,studName)
            s.wfile.write("ipaddr="+ipAddr+",macaddr="+macAddr)

        if s.path[:14] == "/histogramdata":

                #get list of latest ratings
                maxTime = i.get_max_time()
                #print("max time = "+maxTime)
                """
                studentRatings = i.get_time_ratings(maxTime[1][0])
                numStudents = len(studentRatings)

                #set number of bars on graph
                resolution = 10

                frequencyList = []

                #tally up frequency
                increment = numStudents/resolution

                for currentRating in studentRatings:
                    lowNum = 0
                    i = 0;
                    while i < resolution:
                        highNum = lowNum + increment
                        if currentRating <= highNum and currentRating > lowNum:
                            frequencyList[i] += 1
                        i += 1
                        lowNum = highNum



                s.wfile.write("{ \"resolution\":"+resolution+",")
                s.wfile.write("\"frequencies\":"+frequencyList+",")
                s.wfile.write("\"numStudents\":"+numStudents+" }")

                """

                s.wfile.write("{ \"resolution\":10,")
                s.wfile.write("\"frequencies\":[0,0,0,3,5,5,10,15,20,10],")
                s.wfile.write("\"numStudents\":68 }")

        if s.path == '/' or s.path == '':
                #s.wfile.write("the index.html should be printed out now")
                f = open("index.html","r")
                HTML_Text = f.read()
                print(HTML_Text)
                s.wfile.write(HTML_Text)
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
