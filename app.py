from flask import Flask, render_template, jsonify
from database import load_baskets_from_db, load_basket_from_db


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
  



print(__name__)
if __name__=="__main__":
  
  #app.run(host="0.0.0.0",debug=True)
  app.run(host = "0.0.0.0")
