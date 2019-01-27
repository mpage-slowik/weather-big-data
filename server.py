from flask import Flask, jsonify, render_template
from weather.plotting import plotPoints
from  Model import earthquake
import json
app = Flask(__name__)


@app.route("/")
def hello():
    #print(earthquake.getData())
    fig1 = plotPoints()
    return render_template("index.html", fig1=fig1)

# @app.route("/hello")
# def h():
    #return "HEY IM HERE"
    # return jsonify(getData())

if __name__ == '__main__':
    app.run(debug=True)