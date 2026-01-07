import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class HTTPServlet {



    public HttpResponse<String> sendRequest(String url){
    
        try{
                HttpClient client = HttpClient.newHttpClient();
                HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create(url))
                        .GET()
                        .build();

                System.out.println("Connecting to Sportmonks...");
                
                HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
                return response;

        }
        catch(Exception e){
            System.out.println("Connection failed: " + e.getMessage());
            return null;
        }
    }
}
