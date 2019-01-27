from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap
import json
import plotting
app = Flask(__name__)

@app.route("/")
def index():
    cloud = "templates/static/cloud.png"
    water = "templates/static/water-drop.png"
    return render_template("index.html",cloud=cloud, water=water)

@app.route("/Tsunami")
def hur():
   # plotPoints("tsunami",tsunami.getDataTsunami(),'bo')
    return render_template("tsunami.html")

@app.route("/Earthquakes")
def ert():
    #plotPoints("earthquakes",earthquake.getData(),'go')
    return render_template("earthquakes.html")

@app.route("/Weather")
def wea():
    #plotWeather("weather",weather.getHailReports(),weather.getWindReports(),weather.getTornadoReports())
    return render_template("weather.html")

if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)
    #plotting.main()