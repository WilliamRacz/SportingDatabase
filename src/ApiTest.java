import java.net.http.HttpResponse;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class ApiTest {
    public static void main(String[] args) {
        try {
            HTTPServlet http = new HTTPServlet();
            env.load();

            String token = env.get("SPORTMONKS_API_TOKEN");
            if (token == null) {
                System.out.println("ERROR: Token not found");
                return;
            }

            // INPUTS
            long playerId = 52296;   // <-- set player ID
            long seasonId = 16036;   // <-- set season ID



            // CONSTANTS
            String base = "https://api.sportmonks.com/v3/football/";
            String resource = "players/" + playerId;

            // QUERY PARAMS
            String include = "statistics.details.type";
            String filters = "playerStatisticSeasons:" + seasonId + "";

            // BUILD URL (encode include + filters)
            String url = base + resource
                    + "?api_token=" + token
                    + "&include=" + include
                    + "&filters=" + filters;

            // SEND REQUEST
            HttpResponse<String> response = http.sendRequest(url);

            // OUTPUT
            System.out.println("Status: " + response.statusCode());
            System.out.println(response.body());

        } catch (Exception e) {
            System.out.println("Connection failed: " + e.getMessage());
        }
    }
}
