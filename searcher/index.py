from . import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def requests():
    return render_template("results.html")