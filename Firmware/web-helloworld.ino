#include "HttpClient/HttpClient.h"
#include "WebServer.h"
#include "WebServer.h"
#define PREFIX ""
#define INPUT_PIN A0
#define TARGET 192.168.1.1
const float READ_MAX = 4096;

WebServer webserver(PREFIX, 80);
char myIpString[24];
char myMacString[17];   //MAC Address + formatting
char requestbuffer[100];
byte MAC[6];            //Bytes of MAC Address
HttpClient http;
http_request_t request;
http_response_t response;
http_header_t headers[] = {
    { "Accept" , "*/*"},
    { NULL, NULL }
};

TCPClient client;

template<class T>
inline Print &operator <<(Print &obj, T arg)
{ obj.print(arg); return obj; }
int Interest_input = 0;

void helloCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  server.httpSuccess();

  if (type != WebServer::HEAD)
  {
    float output = Interest_input / READ_MAX;
    output *= 10;

    server << output;
  }
}

void setup()
{
  webserver.setDefaultCommand(&helloCmd);
  
  // Report IP address as spark variable, string
  IPAddress myIp = WiFi.localIP();
  sprintf(myIpString, "%d.%d.%d.%d", myIp[0], myIp[1], myIp[2], myIp[3]);
  Spark.variable("ipAddress", myIpString, STRING);
  
  // Report my MAC address as spark variable, string
  WiFi.macAddress(MAC);             //Store in bytes, least to most significant
  sprintf(myMacString, "%x:%x:%x:%x:%x:%x", MAC[5],MAC[4],MAC[3],MAC[2],MAC[1],MAC[0]);
  Spark.variable("macAddress", myMacString, STRING);

  webserver.addCommand("index.html", &helloCmd);

  webserver.begin();
  
  client.connect("TARGET", 80);

  request.hostname = "TARGET";
  request.port = 80;
  
  //Form HTTP Request
  strcpy (requestbuffer,"/registeraddress?ipaddr=");
  strcat (requestbuffer,myIpString);
  strcat (requestbuffer,"&macaddr=");
  strcat (requestbuffer,myMacString);
  request.path = requestbuffer;

  http.get(request, response, headers);
  
  pinMode(INPUT_PIN, INPUT);
}

void loop()
{
  char buff[64];
  int len = 64;

  Interest_input = analogRead(INPUT_PIN);

  webserver.processConnection(buff, &len);
  
  if (client.available())
  {
    client.read();
  }

  if (!client.connected())
  {
    client.stop();
    for(;;);
  }
}
