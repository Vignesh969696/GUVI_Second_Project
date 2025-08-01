import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv(r"D:\guvi_fourth_project\ODI_Match\The_ODI_full_dataset.csv", low_memory=False)

# Clean up common junk values
df = df.replace("None", pd.NA)
df = df.dropna(subset=["match_id"])  
df["match_id"] = df["match_id"].astype(str)

# 1. Top 5 venues by matches hosted
venue_counts = df.dropna(subset=["venue"]).groupby("venue")["match_id"].nunique().sort_values(ascending=False).head(5)
sns.barplot(x=venue_counts.values, y=venue_counts.index, palette='muted')
plt.title("Top 5 ODI Venues by Matches")
plt.xlabel("Match Count")
plt.ylabel("Venue")
plt.show()

# 2. Top 5 teams by match wins
winner_counts = df.dropna(subset=["winner_info"]).groupby("winner_info")["match_id"].nunique().sort_values(ascending=False).head(5)
sns.barplot(x=winner_counts.values, y=winner_counts.index, palette='Blues_d')
plt.title("Top 5 Teams by Wins")
plt.xlabel("Match Wins")
plt.ylabel("Team")
plt.show()

# 3. Toss decisions
toss_decision_counts = df.dropna(subset=["toss_decision_info"]).groupby("toss_decision_info")["match_id"].nunique()
plt.figure(figsize=(6, 6))
plt.pie(toss_decision_counts, labels=toss_decision_counts.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
plt.title("Toss Decision Breakdown")
plt.ylabel("")
plt.show()

# 4. Top 5 Players of the Match
pom_counts = df.dropna(subset=["player_of_match_info"]).groupby("player_of_match_info")["match_id"].nunique().sort_values(ascending=False).head(5)
sns.barplot(x=pom_counts.values, y=pom_counts.index, palette="Greens_d")
plt.title("Top 5 Players of the Match")
plt.xlabel("Awards")
plt.ylabel("Player")
plt.show()

# 5. Toss winner being match winner (barplot for probability per toss decision)
df["toss_winner_won"] = (df["toss_winner_info"] == df["winner_info"]).astype(int)
toss_outcomes = df.dropna(subset=["toss_decision_info"]).groupby("toss_decision_info")["toss_winner_won"].mean()
toss_outcomes.plot(kind="bar", color="brown")
plt.title("Toss Win → Match Win Probability")
plt.ylabel("Probability")
plt.xlabel("Toss Decision")
plt.show()

# 6. Match outcome distribution
def outcome_type(row):
    if pd.notna(row["winner_runs_info"]):
        return "Won by Runs"
    elif pd.notna(row["winner_wickets_info"]):
        return "Won by Wickets"
    else:
        return "No Result"

df["outcome_type"] = df.apply(outcome_type, axis=1)
outcome_counts = df.groupby("outcome_type")["match_id"].nunique()
outcome_counts.plot(kind="bar", color="teal")
plt.title("Match Outcome Distribution")
plt.ylabel("Match Count")
plt.xlabel("Outcome Type")
plt.show()

# 7. Top 5 cities by number of matches
city_counts = df.dropna(subset=["city_info"]).query("city_info != ''").groupby("city_info")["match_id"].nunique().sort_values(ascending=False).head(5)
sns.barplot(x=city_counts.values, y=city_counts.index, palette="Set2")
plt.title("Top 5 Cities by ODI Matches")
plt.xlabel("Match Count")
plt.ylabel("City")
plt.show()

# 8. Runs per ball
df["runs_off_bat"].hist(bins=range(0, 8), color='gray', rwidth=0.9)
plt.title("Runs per Ball")
plt.xlabel("Runs")
plt.ylabel("Ball Count")
plt.show()

# 9. Extras per ball
df["extras"].hist(bins=range(0, 6), color="red", rwidth=0.9)
plt.title("Extras Distribution")
plt.xlabel("Extras")
plt.ylabel("Ball Count")
plt.show()

# 10. Wickets per match
wicket_counts = df.groupby("match_id")["wicket_type"].apply(lambda x: x.notna().sum())
wicket_counts.hist(bins=range(0, 15), color='green', rwidth=0.8)
plt.title("Wickets per Match")
plt.xlabel("Wicket Count")
plt.ylabel("Match Frequency")
plt.show()

