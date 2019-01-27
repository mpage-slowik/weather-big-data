from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap
import json
import os
import plotting
app = Flask(__name__) 
#app.config['UPLOAD_FOLDER']= os.path.join("templates","static")
@app.route("/")
def index():
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

@app.route("/AboutUs")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    Bootstrap(app)
    # print(app.root_path)
    plotting.main()
    app.run(debug=True)

