from flask import render_template
from portfolio import app

@app.route("/")
@app.route("/index",methods=["GET"])
def home():
    return render_template("index.html")

