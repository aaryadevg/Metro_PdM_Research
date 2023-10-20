from flask import Flask, flash, redirect, render_template, request, session, abort
import pathlib

TEMPLATE_DIR = pathlib.Path("templates")
app = Flask(__name__)

@app.route("/")
def index():
    if session.get("logged_in"):
        # Navigate to admin page
        return "Hello"
    else:
        return render_template("login.html")

@app.route("/login/new", methods=["POST"])
def new_user():
    return "TODO: Add User to DB"

@app.route("/login", methods=["POST"])
def login():
    return "TODO: Retrieve data from database"

@app.route("/logout")
def log_out():
    session["logged_in"] = False
    return redirect("/")

@app.route("/mark", methods=["POST"])
def mark_fail():
    return "TODO: mark this ID as a failure"

if __name__ == "__main__":
    app.run(port=4000,
            debug=False)