from flask import Flask, render_template, jsonify

app=Flask(__name__)


Projects = [{
  'id':
  1,
  'title':
  'Exploratory Data Analysis on Brazilian E-Commerce Olist',
  'Libraries':
  'Pandas, Numpy, Matplotlib, Seaborn, Plotly',
  'link':
  'https://jovian.com/outlink?url=https%3A%2F%2Fjovian.ai%2Fyashchamp96%2Fproject-2-exploratory-data-analysis'
}, {
  'id':
  2,
  'title':
  'Exploratory Data Analysis and Visualization of Breast Cancer Data',
  'Libraries':
  'Pandas, Numpy, Matplotlib, Seaborn, Plotly',
  'link':
  ''
}, {
  'id':
  3,
  'title':
  'Automated Web scraping project of Flipkart',
  'Libraries':
  'Pandas, Numpy, Selenium, AWS, Beautifulsoup',
  'link':
  ''
}, {
  'id': 4,
  'title': 'Bulldozer Price Prediction - RandomForestRegressor',
  'Libraries':
  'Pandas, Numpy, Scikit-lear, Matplotlib, Plotly, Randomforest Regression',
  'link': ''
}]


    
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", projects=Projects)

@app.route("/aboutme")
def about():
    return render_template("aboutme.html")

if __name__== "__main__":
    app.run(debug=True)

