from flask import Flask, jsonify, render_template
from initial import getData
from plotting import build_plot
#from bokeh import 
import json
app = Flask(__name__)

@app.route('/plot')
def render_plot():
    plot_snippet = build_plot()
    
    return render_template('plots.html', snippet=plot_snippet)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/hello")
def h():
    #return "HEY IM HERE"
    return jsonify(getData())

if __name__ == '__main__':
    app.run(debug=True)