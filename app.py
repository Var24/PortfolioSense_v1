from flask import Flask, render_template, jsonify
from database import load_baskets_from_db


app = Flask(__name__)
     

@app.route("/")
def hello_baskets():
  baskets = load_baskets_from_db()
  return render_template("home.html",portfolios=baskets)

@app.route("/api/baskets")
def list_baskets():
  baskets = load_baskets_from_db()
  return jsonify(baskets)

print(__name__)
if __name__=="__main__":
  
  #app.run(host="0.0.0.0",debug=True)
  app.run(host = "0.0.0.0")
