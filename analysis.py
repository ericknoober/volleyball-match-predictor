import pandas as pd

#load match data
matches = pd.read_csv("matchStats.csv")

#determining each team's home wins
#checking if the winner column is the same as the home team to determine
#home wins and then converting the boolean to an integer
#Home team win is 1, 0 is away team win
matches["Home_Win"] = (matches["Winner"] == matches["Home Team"]).astype(int)

#home team win rate calculation
#using pandas functions that calculates mean since data is in ones and zeroes
home_win_rate = matches["Home_Win"].mean() * 100

#average out the stats when the home team wins vs loses
#list of stats
stats = ["Kills Home", "Blocks Home", "Aces Home", "Digs Home"]
print("\nAverage stats when Home Team wins vs loses:")
#sorts the matches into two groups, wins vs loses
#looks only at the four groups in the stats list
#determines the mean for each group
#rounds by two decimal places to clean up
print(matches.groupby("Home_Win")[stats].mean().round(2))

#home and away win rate
away_win_rate = 100 - home_win_rate
print("Home team win rate: " , home_win_rate)
print("Away team win rate: " , away_win_rate)

#table of home wins 
print("Home wins by team")
#groups matches by team, and gets their home wins to sum them together
#Then sorts them by descending order
print(matches.groupby("Home Team")["Home_Win"].sum().sort_values(ascending=False))


# merging home and away columns into one
home = matches[["Home Team", "Away Team", "Kills Home", 
                "Blocks Home", "Aces Home", "Home_Win"]].copy()
home.columns = ["Team", "Opponent", "Kills", "Blocks", "Aces", "Won"]

away = matches[["Away Team", "Home Team", "Kills Away", 
                "Blocks Away", "Aces Away"]].copy()
away["Won"] = 1 - matches["Home_Win"]  # flip the result for away team
away.columns = ["Team", "Opponent", "Kills", "Blocks", "Aces", "Won"]

# combine data into one column
all_teams = pd.concat([home, away], ignore_index=True)

#corr() function determines which stats correlate with home wins
correlation_all = all_teams[["Won", "Kills", "Blocks", "Aces"]].corr()["Won"].sort_values(ascending=False)
print("\nCorrelation with winning (all teams):")
print(correlation_all.round(3))
