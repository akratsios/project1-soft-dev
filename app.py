from flask import Flask, render_template, request, session, redirect, url_for
import random
import login
import utils

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    if 'user' not in session:
        session['user'] = 0
    user = session['user']
    return render_template("home.html", user = user)
        
@app.route("/login",methods=['GET', 'POST'])
def log_in():
    if request.method == "GET":
        if (session['user'] != 0):
            return redirect(url_for("home"))
        #post the form
        user = session['user']
        return render_template("login.html", user = user, extra = "")
    else:
        user = request.form["user"]
        pwd = request.form["pass"]
        submit = request.form["action"]
        if (user == "" or pwd == ""):
            return render_template("login.html", user = user, extra = "Try again")
        if (submit == "Login"):
            result = login.checkuser(user,pwd)
            print result
            if (result == "in"):
                session['user'] = user
                return redirect(url_for("home"))
            else:
                session['user'] = 0
                user = session['user']
                return render_template("login.html", user = user, extra = result)
        else:
            login.adduser(user,pwd)
            session['user'] = user
            return redirect(url_for("home"))

@app.route("/logout")
def logout():
    #resets the session to none
    session['user'] = 0
    print (session['user'])
    return redirect(url_for("log_in"))


@app.route("/create",methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        if (session['user'] == 0):
            return redirect(url_for("home"))
        return render_template("create.html")
    if request.method == "POST":
        return render_template("blog.html", user = user)

@app.route("/blog",methods=['GET', 'POST'])
def blog():
    if request.method == "GET":
        #supposed to read the sql tables and display blogs with 10 per page
        user = session['user']
        blogs = utils.getblogs(1,10);
        return render_template("blog.html", user = user, blogs = blogs)
    if request.method == "POST":
        user = session['user']
        blogs = utils.getblogs(10,20);
        page = True;
        return render_template("blog.html", user = user, blogs = blogs, page = page)

@app.route("/comment",methods=['GET', 'POST'])
def comment():
    user = session['user']
    #temp for testing
    comments = utils.getblogcomments(2);
    return render_template("comment.html", user = user, comments = comments)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "shh"
    app.run(host = '0.0.0.0', port = 8000)

