from flask import Flask, jsonify, render_template
from plotting import plotPoints
import json
app = Flask(__name__)


@app.route("/")
def hello():
    graph1_url=plotPoints()
    return render_template("index.html",
    graph1=graph1_url.show(),)

# @app.route("/hello")
# def h():
    #return "HEY IM HERE"
    #return jsonify(getData())

if __name__ == '__main__':
    app.run(debug=True)