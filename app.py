from flask import Flask, render_template, jsonify

app=Flask(__name__)


    
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", projects=Projects)

@app.route("/aboutme")
def about():
    return render_template("aboutme.html")

if __name__== "__main__":
    app.run(debug=True)

