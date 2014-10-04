// This #include statement was automatically added by the Spark IDE.
#include "WebServer.h"

/* Web_HelloWorld.pde - very simple Webduino example */

#include "WebServer.h"

/* This creates an instance of the webserver.  By specifying a prefix
 * of "", all pages will be at the root of the server. */
#define PREFIX ""
#define INPUT_PIN A0
const float READ_MAX = 4096; //Float to handle casting correctly
WebServer webserver(PREFIX, 80);

template<class T>
inline Print &operator <<(Print &obj, T arg)
{ obj.print(arg); return obj; }

int Interest_input = 0;
/* commands are functions that get called by the webserver framework
 * they can read any posted data from client, and they output to the
 * server to send data back to the web browser. */
void helloCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  /* this line sends the standard "we're all OK" headers back to the
     browser */
  server.httpSuccess();

  /* if we're handling a GET or POST, we can output our data here.
     For a HEAD request, we just stop after outputting headers. */
  if (type != WebServer::HEAD)
  {
    float output = Interest_input / READ_MAX;
    output *= 10;
    /* this defines some HTML text in read-only memory aka PROGMEM.
     * This is needed to avoid having the string copied to our limited
     * amount of RAM. */

    server << output;

    /* this is a special form of print that outputs from PROGMEM */
    //server.printP(helloMsg);
  }
}

void setup()
{
  /* setup our default command that will be run when the user accesses
   * the root page on the server */
  webserver.setDefaultCommand(&helloCmd);

  /* run the same command if you try to load /index.html, a common
   * default page name */
  webserver.addCommand("index.html", &helloCmd);

  /* start the webserver */
  webserver.begin();
  
  pinMode(INPUT_PIN, INPUT);
}

void loop()
{
  char buff[64];
  int len = 64;

  Interest_input = analogRead(INPUT_PIN);
  /* process incoming connections one at a time forever */
  webserver.processConnection(buff, &len);
}
