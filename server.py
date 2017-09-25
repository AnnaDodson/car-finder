from flask import Flask
from flask import render_template
app = Flask(__name__)
import sortCars

@app.route("/")
def hello(name=None):
    carList = sortCars.getTopCars()
    return render_template("base.html", cars=carList)
    
