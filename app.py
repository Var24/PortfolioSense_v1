from flask import Flask, render_template, jsonify

app = Flask(__name__)

baskets = [{
  'ID': 1,
  'title': 'Low Volatility',
  'benchmark': 'BSE 100',
  'Methodology': 'Volatility based weighting',
  'No of constituents': '30'
},
{
  'ID': 2,
  'title': 'Momentum',
  'benchmark': 'BSE 200',
  'Methodology': 'Tilt based weighting',
  'No of constituents': '30'
},
{
  'ID': 3,
  'title': 'High Quality',
  'benchmark': 'BSE 100',
  'Methodology': 'Tilt based weighting',
  'No of constituents': '30'
},
{
  'ID': 4,
  'title': 'Dividend Income',
  'benchmark': 'BSE 100',
  'Methodology': 'Periodic capped free float Mcap',
  'No of constituents': '50'           
}]


@app.route("/")
def hello_world():
  return render_template("home.html",portfolios=baskets)

@app.route("/api/baskets")
def list_baskets():
  return jsonify(baskets)

print(__name__)
if __name__=="__main__":
  #print("inside the if now")
  app.run(host="0.0.0.0",debug=True)
