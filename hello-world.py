from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about_page():
    return "<h1>Hi!</h1>\n<h2>My name is Yossi Bengaev & I'm learning devops in Bynet!</h2>"

