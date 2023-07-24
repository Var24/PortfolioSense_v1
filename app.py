from flask import Flask, render_template, jsonify, request
from database import load_baskets_from_db, load_basket_from_db
import pandas as pd

app = Flask(__name__)
     

@app.route("/")
def hello_baskets():
  baskets = load_baskets_from_db()
  return render_template("home.html",portfolios=baskets)

@app.route("/api/baskets")
def list_baskets():
  baskets = load_baskets_from_db()
  return jsonify(baskets)
  
@app.route("/basket/<ID>")
def show_basket(ID):
  basket = load_basket_from_db(ID)
  if not basket:
    return "Not Found",404
  return render_template("basketpage.html",basket=basket)

@app.route("/sense")
def index():
  return render_template("form.html")

@app.route('/process', methods=['POST'])
def process():
    stock_names = request.form['stock_names']
    weights = request.form['weights']

    # Convert input strings into lists
    stock_names = stock_names.split(',')
    weights = weights.split(',')

    # Create a DataFrame from the user inputs
    data = {'Stock Name': stock_names, 'Weight': weights}
    df = pd.DataFrame(data)

    return df.to_html()

  



print(__name__)
if __name__=="__main__":
  
  #app.run(host="0.0.0.0",debug=True)
  app.run(host = "0.0.0.0")
