
from flask import Flask, request, render_template, jsonify, redirect, session
import joblib
import pandas as pd
import numpy as np
import pymysql

model = joblib.load("best_model_rf.pkl")
# scaler = joblib.load("scaler.pkl")

app = Flask(__name__, static_url_path="/static")
app.secret_key = "aspallegend"

# Database connection settings
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "naveenpalani75@"
DB_NAME = "lever"

# Ensure database and tables exist
def create_database_and_table():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    cur = conn.cursor()
    
    # Create database if it doesn't exist
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    
    # Connect to the newly created database
    conn.select_db(DB_NAME)
    
    # Create the 'users' table if it doesn't exist
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

# Run the database creation on startup
create_database_and_table()

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/rendersignup")
def rendersignup():
    return render_template("signup.html")

@app.route("/renderlogin")
def renderlogin():
    return render_template("login.html")

@app.route("/accuracy")
def accuracy():
    return render_template("accuracy.html")

@app.route("/signup", methods=["POST"])
def signup():
    payload = request.json
    name = payload["name"]
    email = payload["email"]
    password = payload["password"]

    if email_exists(email):
        return jsonify({"result": "Email already exists"})

    if create_user(name, email, password):
        return jsonify({"result": "signup success"})

    return jsonify({"result": "signup failed"})

def email_exists(email):
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM `users` WHERE `email` = %s", (email,))
    output = cur.fetchall()
    conn.close()
    return len(output) > 0

def create_user(name, email, password):
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
    )

    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO `users` (`name`, `email`, `password`) VALUES (%s, %s, %s)",
            (name, email, password),
        )
        conn.commit()
        return cur.rowcount > 0
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

@app.route("/login", methods=["POST"])
def login():
    payload = request.json
    email = payload["email"]
    password = payload["password"]
    rawData = login1(email, password)
    if len(rawData) == 0:
        return {"result": "login unsuccess"}
    else:
        return {"result": "login success"}

def login1(email, password):
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
    )

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM `users` WHERE `email` = %s AND `password` = %s",
        (email, password),
    )
    output = cur.fetchall()
    conn.close()
    return output

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("welcome.html")

@app.route("/predict", methods=["POST"])
def predict_disease():
    payload = request.json
    AAP = payload["AAP"]
    SGPT = payload["SGPT"]
    TB = payload["TB"]
    DB = payload["DB"]
    SGOT = payload["SGOT"]
    AGR = payload["AGR"]
    ALBA = payload["ALBA"]
    AGE = payload["AGE"]
    GEN = payload["GEN"]
    TP = payload["TP"]

    input_arr = np.array(
        [AGE, GEN, TB, DB, AAP, SGPT, SGOT, TP, ALBA, AGR], dtype=float
    )
    input_arr[1] = int(input_arr[1])
    result = model.predict([input_arr])[0]

    if result == 0:
        return jsonify({"message": "Liver Disease please consult doctor.", "status": "danger"})
    if result == 1:
        return jsonify({"message": "You are strong and Healthy.", "status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
