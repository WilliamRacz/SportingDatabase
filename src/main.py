import env
from HTTPHelper import send_request
from funcHelper import build_url, get_player_season_row, build_season_list
env.load()
import json
token = env.get("SPORTMONKS_API_TOKEN")

player_id = 52296
season_id = 16036
teamId = 20

base = "https://api.sportmonks.com/v3/football/"
resource = f"players/{player_id}"
include = "statistics.season"
filters = f"playerStatistics"
filters = None




#Functions:
#build_url              - Given base resource include filter strings    ->  returns HTTP String ready to send
#get_player_season_row  - Given Season_id, player_id                    ->  returns player/Season row of statistics
#build_season_list      - Given a player_id                             ->  returns list of seasons



#seasonPlayerRow = get_player_season_row(player_id, season_id, token)

ul = build_url(base, resource, token, include, filters)
data = send_request(ul) 






player_seasons = build_season_list(data)

print(player_seasons)