from flask import Flask
from initial import getData
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def h():
    return "HEY IM HERE"
    #return getData()

if __name__ == '__main__':
    app.run(debug=True)