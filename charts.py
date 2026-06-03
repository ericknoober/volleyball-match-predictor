#imports
import pandas as pd
import plotly.express as px

matches = pd.read_csv("matchStats.csv")
matches["Home_Win"] = (matches["Winner"] == matches["Home Team"]).astype(int)

# filtering home and away data into one column
#copid from analysis.py
home = matches[["Home Team", "Away Team", "Kills Home",
                "Blocks Home", "Aces Home", "Home_Win"]].copy()
home.columns = ["Team", "Opponent", "Kills", "Blocks", "Aces", "Won"]

away = matches[["Away Team", "Home Team", "Kills Away",
                "Blocks Away", "Aces Away"]].copy()
away["Won"] = 1 - matches["Home_Win"]
away.columns = ["Team", "Opponent", "Kills", "Blocks", "Aces", "Won"]

all_teams = pd.concat([home, away], ignore_index=True)

# Chart 1

#data from analysis.py
df_corr = pd.DataFrame({"Stat" : ["Aces", "Blocks", "Kills"], 
                        "Correlation" : [0.353, 0.210, 0.166]
                        })

#chart description
fig1 = px.bar(df_corr, x="Stat", y="Correlation", 
              title="Which stats best predict winning", 
              color="Correlation", color_continuous_scale="blues", 
              text="Correlation")

#display chart
fig1.show()

#Chart 2 - home/away win rate

#used data from analysis.py
win_data = pd.DataFrame({
    "Location": ["Home", "Away"],
    "Win Rate": [37.1, 62.9]
})

#created chart
fig2 = px.bar(
    win_data,
    x="Location",
    y="Win Rate",
    title="Home vs Away Win Rate (VNL 2025)",
    color="Location",
    color_discrete_map={"Home": "#636EFA", "Away": "#EF553B"},
    text="Win Rate"
)

#displaying chart
#adds percentage sign
fig2.update_traces(texttemplate="%{text}%", textposition="outside")
fig2.update_layout(yaxis_range=[0, 100])
fig2.show()

#Chart 3 - top teams by wins

#import teams data
teams = pd.read_csv("teamStats.csv")

#Created chart
fig3 = px.bar(
    teams.sort_values("Won", ascending=False),
    x="Team",
    y="Won",
    title="VNL 2025 Team Wins",
    color="Won",
    color_continuous_scale="blues",
    text="Won"
)

#display chart
fig3.update_traces(textposition="outside")
#rotates labels by 45 degrees
fig3.update_layout(xaxis_tickangle=-45)
fig3.show()
