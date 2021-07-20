from logging import debug
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to my Flask Page!"

@app.route("/data")
def data():
    return "Welcome to my data!"

@app.route("/read")
def read():
    """Read all data from an SQL Table"""
    return "Welcome to my Flask Page!"

@app.route("/write")
def write():
    """Write data to an SQL Table"""
    return "Welcome to my data!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

