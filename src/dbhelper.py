# DBHelper.py

import psycopg2
import sys

def connect_db(db_name, user, password, host="localhost", port="5432"):
    """
    Open a connection to PostgreSQL and return the connection object.
    Kill the script on failure (brute-force simple).
    """
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("PostgreSQL connection established.")
        return conn

    except psycopg2.Error as e:
        print(f"[DB ERROR] {e}")
        sys.exit(1)

PLAYER_SEASON_INSERT = """
    INSERT INTO player_season_stats (
        player_id, season_id, team_id,
        appearances, minutes_played, goals, shots_total, shots_on_target,
        passes, accurate_passes, accurate_passes_percentage, key_passes,
        dribble_attempts, succ