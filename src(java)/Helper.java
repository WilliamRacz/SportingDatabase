import java.net.http.HttpResponse;

public class Helper {

    private final HTTPServlet http;
    private final String base;
    private final String token;

    public Helper(String token, HTTPServlet http) {
        this.http = http;
        this.token = token;
        this.base = "https://api.sportmonks.com/v3/football/";
    }

    // --- core generic helper (accepts any resource, include, filters) ---
    public HttpResponse<String> call(
            String resource,
            String include,
            String filters
    ) {

        StringBuilder url = new StringBuilder(base)
                .append(resource)
                .append("?api_token=").append(token);

        if (include != null && !include.isEmpty()) {
            url.append("&include=").append(include);
        }

        if (filters != null && !filters.isEmpty()) {
            url.append("&filters=").append(filters);
        }

        return http.sendRequest(url.toString());
    }


    // --- convenience endpoint: Player Season Stats ---
    public HttpResponse<String> getPlayerSeasonStats(long playerId, long seasonId) {
        return call(
                "players/" + playerId,
                "statistics.details.type",
                "playerStatisticSeasons:" + seasonId
        );
    }

    public HttpResponse<String> getTeamSquad(long teamId, long seasonId) {
        // Endpoint: /squads/seasons/{seasonID}/teams/{teamID}
        String resource = "squads/seasons/" + seasonId + "/teams/" + teamId;
    
        // include=player gives you player details (name, dob, etc.)
        String include = "player";
        String filters = null; // none needed here
    
        return call(resource, include, filters);
    }
}
