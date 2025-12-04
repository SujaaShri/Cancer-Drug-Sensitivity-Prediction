from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = r"C:\Users\sachu_svqxcy3\OneDrive\Desktop\ML_Project"

@app.route("/")
def index():
    return render_template("predict.html")

@app.route("/data")
def data():
    return send_from_directory(BASE_DIR, "GDSC_ML.csv")

if __name__ == "__main__":
    app.run(debug=True)
