from flask import flask
app = Flask(__name__)
@app.route(/)
def home_view():
    return "<h1> Welcome to my new app</h1>"
    