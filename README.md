# volleyball-match-predictor

Python data analysis project which predicts match outcomes using 2025 Men's VNL data. Built using panadas, plotly, and streamlit.

## Features
- Select two 2025 VNL men's teams
- Confidence score calculated using season average stats
- Prediction history saved to SQLite database

## Current Findings
- Away team tends to win 63% of VNL matches, could mean that home court advantage is nonexistent or error with data
- Initally used home win data only for correlation of wins and stats, but analyzing all teams revelaed aces are a strong predictor of winning
- Using a logisitc regression model to train data, achieving a accuracy score of 87.5% which predicts outcome based on the stats of the match (does not tell us much, but will build a model that predicts outcomes using pre-match averages
- pre-match prediction model gives confidences levels of 52%-54%; suggests raw averages is insufficent data

## How to run
Installing dependices: pip3 install pandas plotly scikit-learn fastapi uvicorn

## API Endpoints
- GET /teams — returns all 18 VNL teams
- GET /predict?home=X&away=Y — predicts match winner with confidence score
- GET /history — returns all past predictions with timestamps

## Charts
<img width="1444" height="692" alt="image" src="https://github.com/user-attachments/assets/67600111-e4ac-450b-bc63-8bc7c820ac79" />

<img width="1455" height="713" alt="image" src="https://github.com/user-attachments/assets/a6de0352-c0b6-40f1-82fc-b1814e8fad9e" />

<img width="1444" height="711" alt="image" src="https://github.com/user-attachments/assets/09fdfe7c-5874-48df-b6a2-be48262a045d" />

frontend sample
<img width="974" height="554" alt="image" src="https://github.com/user-attachments/assets/e04b8db6-b907-4081-befd-257a990a067b" />

