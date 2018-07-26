from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
def hello(name='World'):
    return "Hello {}!".format(name)


@app.route("/error")
def error(showme='hi debugger'):
    raise ValueError('Deliberate error for testing purposes!')
