import sqlite3

conn = sqlite3.connect("D:/guvi_fourth_project/cricket_data.db")
cursor = conn.cursor()

# Helper function
def run_query(title, query):
    print(f"{title}")
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Error:", e)
    print("-" * 30)

print("\nODI QUERIES")

run_query("1. Top 5 venues", "SELECT venue, COUNT(DISTINCT match_id) FROM odi_matches GROUP BY venue ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("2. Top 5 teams by wins", "SELECT winner_info, COUNT(DISTINCT match_id) FROM odi_matches WHERE winner_info IS NOT NULL GROUP BY winner_info ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("3. Toss decisions", "SELECT toss_decision_info, COUNT(DISTINCT match_id) FROM odi_matches GROUP BY toss_decision_info;")
run_query("4. Player of the match", "SELECT player_of_match_info, COUNT(DISTINCT match_id) FROM odi_matches WHERE player_of_match_info IS NOT NULL GROUP BY player_of_match_info ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("5. Toss winner being match winner", "SELECT COUNT(DISTINCT match_id) FROM odi_matches WHERE toss_winner_info = winner_info;")
run_query("6. Match outcome distribution", "SELECT CASE WHEN winner_runs_info IS NOT NULL THEN 'Won by Runs' WHEN winner_wickets_info IS NOT NULL THEN 'Won by Wickets' ELSE 'No Result' END AS outcome_type, COUNT(DISTINCT match_id) FROM odi_matches GROUP BY outcome_type;")
run_query("7. Top 5 cities", "SELECT city_info, COUNT(DISTINCT match_id) FROM odi_matches WHERE city_info IS NOT NULL AND city_info != 'None' AND TRIM(city_info) !='' GROUP BY city_info ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")


print("\nT20 QUERIES")
run_query("1. Top 5 venues", "SELECT venue, COUNT(DISTINCT match_id) FROM t20_matches GROUP BY venue ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("2. Top 5 teams by wins", "SELECT match_winner, COUNT(DISTINCT match_id) FROM t20_matches WHERE match_winner IS NOT NULL GROUP BY match_winner ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("3. Toss decision counts", "SELECT toss_decision, COUNT(DISTINCT match_id) FROM t20_matches GROUP BY toss_decision;")
run_query("4. No result matches", "SELECT COUNT(DISTINCT match_id) FROM t20_matches WHERE match_winner IS NULL;")
run_query("5. Top 5 batting teams", "SELECT batting_team, COUNT(DISTINCT match_id) FROM t20_matches GROUP BY batting_team ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("6. Average runs per ball", "SELECT AVG(runs) FROM t20_matches;")
run_query("7. Powerplay deliveries", "SELECT COUNT(*) FROM t20_matches WHERE powerplay = 1;")


print("\nTEST QUERIES")
run_query("1. Top 5 venues", "SELECT venue, COUNT(DISTINCT match_id) FROM test_matches GROUP BY venue ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("2. Top 5 teams by wins", "SELECT match_winner, COUNT(DISTINCT match_id) FROM test_matches WHERE match_winner IS NOT NULL GROUP BY match_winner ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("3. Toss decisions", "SELECT toss_decision, COUNT(DISTINCT match_id) FROM test_matches GROUP BY toss_decision;")
run_query("4. Toss winner also being match winner", "SELECT COUNT(DISTINCT match_id) FROM test_matches WHERE toss_winner = match_winner;")
run_query("5. Top 5 batting teams", "SELECT batting_team, COUNT(DISTINCT match_id) FROM test_matches GROUP BY batting_team ORDER BY COUNT(DISTINCT match_id) DESC LIMIT 5;")
run_query("6. Average runs per ball", "SELECT AVG(runs) FROM test_matches;")



conn.close()
