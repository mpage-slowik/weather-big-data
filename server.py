from flask import Flask, jsonify, render_template
import json
app = Flask(__name__)


@app.route("/")
def hello():
    #print(earthquake.getData())
    #fig1 = plotPoints()
    return render_template("index.html")

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
    app.run(debug=True)