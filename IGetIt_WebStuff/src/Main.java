import java.net.*;

import com.sun.net.httpserver.*;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			HttpServer webServer = HttpServer.create(new InetSocketAddress("127.0.0.1",80),256);
		}
		
		catch (Exception e)
		{
			System.out.println(e);
		}

	}

}
