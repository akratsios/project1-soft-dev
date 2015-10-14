from flask import Flask, render_template, request, session, redirect, url_for
import  random

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    return redirect(url_for("login"))


@app.route("/create",methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        #if not logged in, return login page; to be done when finished
        return render_template("create.html")
    if request.method == "POST":
        return render_template("blog.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")





if __name__ == "__main__":
    app.debug = True
    app.secret_key = "shh"
    app.run(host = '0.0.0.0', port = 8000)
