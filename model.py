#using logisitc regression to predict wins
#gathers all stats from all 116 matches and 
#uses these historical pattern to determine which
#team is more likely to win

#prepare data
#Train model
#Predict

#imports
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

#load data
matches = pd.read_csv("matchStats.csv")

#home win column
matches["Home_Win"] = (matches["Winner"] == matches["Home Team"]).astype(int)

#features used to predict
features = ["Kills Home", "Blocks Home", "Aces Home",
            "Kills Away", "Blocks Away", "Aces Away"]

X = matches[features]
y = matches["Home_Win"]

#splits data into training and testing
#uses 80% of data for training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=15)

#train model
model = LogisticRegression()
model.fit(X_train, y_train)

#test accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy:  {accuracy * 100:.1f}%")

#save model
#uses pickle to convert model to binary file
with open("model.pk1", "wb") as f:
        pickle.dump(model, f)

    


