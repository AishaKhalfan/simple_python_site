from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import json

# Create a Blueprint instance
views = Blueprint("views", __name__)

# Create a route
@views.route("/")
def home():
    return render_template("index.html", name = "Aisha", age = 40)

# Create another route
@views.route("/home")
def home2():
    return "This is the Homepage2!" 

# @views.route("/profile1/<username>")
# def profile(username):
    # return render_template("index.html", name = username) 

@views.route("/about")
def about():
    args = request.args
    name = args.get("name")
    age = args.get("age")
    return render_template("index.html", name = name, age = age) 

@views.route("/profile")
def profile():
    return render_template("profile.html") 

@views.route("/json")
def get_json():
    return {"name": "Aisha", "coolness": 40}

@views.route("/data")
def get_data():
    # data = {"name": "Aisha", "coolness": 40}
    data = request.json
    # return jsonify({"name": "Aisha", "coolness": 40})
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))

