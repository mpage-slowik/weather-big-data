from flask import Flask, jsonify, render_template
from weather.plotting import plotPoints
from  Model import earthquake
import json
app = Flask(__name__)


@app.route("/")
def hello():
    #print(earthquake.getData())
    #fig1 = plotPoints()

    return render_template("index.html")

@app.route("/Huricanes")
def hur():
    plotPoints("huricanes")
    return render_template("huricanes.html")

@app.route("/Earthquakes")
def ert():
    plotPoints("earthquakes")
    return render_template("earthquakes.html")

@app.route("/Weather")
def wea():
    plotPoints("weather")
    return render_template("weather.html")

if __name__ == '__main__':
    app.run(debug=True)