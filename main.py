from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd 
import pickle

app = FastAPI()

#connects frontend to backend
app.add_middleware(CORSMiddleware, allow_origins=["*"], 
                    allow_methods=["*"], allow_headers=["*"])

#load trained model
with open("model.pk1", "rb") as f:
    model = pickle.load(f)

#load match stats
matches = pd.read_csv("data/matchStats.csv")
matches["Home_Win"] = (matches["Winner"] == matches["Home Team"]).astype(int)

#calculate averages per team in all matches

home_stats = matches.groupby("Home Team")[["Kills Home", "Blocks Home", "Aces Home"]].mean()
home_stats.columns = ["Kills", "Blocks", "Aces"]

away_stats = matches.groupby("Away Team")[["Kills Away", "Blocks Away", "Aces Away"]].mean()
away_stats.columns = ["Kills", "Blocks", "Aces"]

#combine home and away stats
team_stats=(home_stats + away_stats)/2

#list of all teams
teams= sorted(matches["Home Team"].unique().tolist())

#/teams and /predict are endpoints to get information called upon

@app.get("/teams")
def get_teams():
    return {"teams" : teams}

@app.get("/predict")
def predict(home: str, away: str):
    #average stats for each team
    home_avg = team_stats.loc[home]
    away_avg = team_stats.loc[away]

    #create all input rows for model
    input_data = pd.DataFrame([{
        "Kills Home": home_avg["Kills"],
        "Blocks Home": home_avg["Blocks"],
        "Aces Home": home_avg["Aces"],
        "Kills Away": away_avg["Kills"],
        "Blocks Away": away_avg["Blocks"],
        "Aces Away": away_avg["Aces"]
    }])

    #make prediction
    #gets first value from array
    prediction = model.predict(input_data)[0]
    #gathers probability
    probability = model.predict_proba(input_data)[0]

    #determines winner
    if prediction == 1:
        winner = home
    else:
        winner = away

    #gets the probability of the team with the 
    #higher chance of winning
    confidence = round(max(probability) * 100, 1)

    return{
        "home": home,
        "away": away,
        "predicted_winner": winner,
        "confidence": f"{confidence}%"
    }
    


