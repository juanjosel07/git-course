
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Principal!"

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/sum/<int:x>/<int:y>")
def sum(x, y):
    return f"suma igual: {str(x + y)}"