from flask import render_template
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Jesper"}
    posts = [
        {
            "author":{"username":"John"},
            "body":"A beautiful day"
        },
        {
            "author":{"username":"Susan"},
            "body":"Keep on trucking"
        }
    ]
    return render_template('index.html', title = "Home", user=user, posts=posts)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)