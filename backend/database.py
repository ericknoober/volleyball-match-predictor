import sqlite3
from datetime import datetime

#connect to database
def get_connection():
    conn = sqlite3.connect("predictiona.db")
    return conn

#create predictions table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            home_team TEXT,
            away_team TEXT,
            predicted_winner TEXT,
            confidence TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

    #save prediction to database
def save_prediction(home, away, winner, confidence):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions 
    (home_team, away_team, predicted_winner, 
                    confidence, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (home, away, winner, confidence, 
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    conn.commit()
    conn.close()

#get all past predictions
def get_predictions():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("select * from predictions")
    rows = cursor.fetchall()
    
    conn.close()
    return rows

#initalize table
create_table()
