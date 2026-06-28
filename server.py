from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index ():
    #hier bekommt unser server the index html seite und gibt gleichzeitig varriablen an die html seite 
    name = "nico"
    age = 16
    return render_template("index.html", name=name, age=age)

@app.route("/route-testing")
def rt():
    return render_template("route_test.html")



if __name__ in "__main__":
    app.run(debug=True)