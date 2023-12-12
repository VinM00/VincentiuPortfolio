"""This part of the script handles Flask servers and renders the portfolio page"""
from flask import Flask, render_template, request
import datetime as dt


app=Flask(__name__)

   
@app.route("/")
@app.route("/home")
def home():
  "read home.html template"
  return render_template("home.html", year=dt.datetime.now().year)

@app.route("/projects")
def portfolio():
  return render_template("projects.html")


if __name__== "__main__":
  app.run(debug=True)