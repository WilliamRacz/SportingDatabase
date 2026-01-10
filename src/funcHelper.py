from HTTPHelper import send_request
import env
import json
env.load()
token = env.get("SPORTMONKS_API_TOKEN")



base = "https://api.sportmonks.com/v3/football/"



def player_season_stats(player_id, season_id):
    resource = f"players/{player_id}"
    include = "statistics.details.type"
    filters = f"playerStatisticSeasons:{season_id}"
    return build_url(base, resource, token, include, filters)


def get_player_season_row(player_id, season_id, token):
    url = player_season_stats(player_id, season_id)
    response = send_request(url)
    
    data = response.json() 
    details = data["data"]["statistics"][0]["details"]
    stats = {}
    for d in details:
        code = d["type"]["code"]
        value = d["value"]

        
                
        if isinstance(value, dict) and "total" in value:
            value = value["total"]

        stats[code] = value
    row = [
        season_id,
        stats.get("appearances"),
        stats.get("minutes-played"),
        stats.get("goals"),
        stats.get("shots-total"),
        stats.get("shots-on-target"),
        stats.get("passes"),
        stats.get("accurate-passes"),
        stats.get("accurate-passes-percentage"),
        stats.get("key-passes"),
        stats.get("dribble-attempts"),
        stats.get("successful-dribbles"),
        stats.get("tackles"),
        stats.get("interceptions"),
        stats.get("clearances"),
        stats.get("total-duels"),
        stats.get("duels-won"),
        stats.get("aeriels-won"),
        stats.get("fouls"),
        stats.get("dispossessed"),
        stats.get("total-crosses"),
        stats.get("accurate-crosses"),
    ]
    return row




def build_url(base, resource, token, include=None, filters=None):
    url = f"{base}{resource}?api_token={token}"
    if include:
        url += f"&include={include}"
    if filters:
        url += f"&filters={filters}"
    return url



def build_season_list(data):
    data = json.loads(data.text)
    num_seasons = len(data['data']['statistics'])
    season_list = []



    for x in range(num_seasons):
        season_list.append(data['data']['statistics'][x]['season_id'])

    return season_list


