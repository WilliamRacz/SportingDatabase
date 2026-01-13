# create_tables.py
from dbhelper import connect_db

def create_tables(conn):
    cur = conn.cursor()


    # 1) leagues
    cur.execute("""
        CREATE TABLE IF NOT EXISTS leagues (
            league_id   BIGINT PRIMARY KEY,
            name        TEXT
        );
    """)

    # 2) seasons
    cur.execute("""
        CREATE TABLE IF NOT EXISTS seasons (
            season_id   BIGINT PRIMARY KEY,
            league_id   BIGINT REFERENCES leagues(league_id),
            name        TEXT,
            start_date  DATE,
            end_date    DATE
        );
    """)

    # 3) teams
    cur.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            team_id     BIGINT PRIMARY KEY,
            name        TEXT,
            league_id   BIGINT REFERENCES leagues(league_id)
        );
    """)

    # 4) players
    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            player_id     BIGINT PRIMARY KEY,
            first_name    TEXT,
            last_name     TEXT,
            display_name  TEXT,
            country       TEXT
        );
    """)

    # 5) player_season_stats (wide table)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS player_season_stats (
            player_id   BIGINT REFERENCES players(player_id),
            season_id   BIGINT REFERENCES seasons(season_id),
            team_id     BIGINT REFERENCES teams(team_id),

            appearances INT,
            minutes     INT,
            goals       INT,
            assists     INT,
            shots_total INT,
            shots_on_target INT,
            passes      INT,
            accurate_passes INT,
            pass_accuracy NUMERIC,
            
            PRIMARY KEY (player_id, season_id, team_id)
        );
    """)

    conn.commit()
    cur.close()
    print("Tables created (or already existed).")

if __name__ == "__main__":
    conn = connect_db("your_db_name", "your_user", "your_password")
    create_tables(conn)
    conn.close()
