from flask import Flask, render_template, url_for
from flask_restful import Resource, Api
import sys
import os

app = Flask(__name__)

@app.route("/")
def Capstone():
    return render_template("main.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/product1/")
def product1():
    return render_template("product1.html")

@app.route("/product2/")
def product2():
    return render_template("product2.html")

if __name__ == "__main__":
    app.run(debug=True)
