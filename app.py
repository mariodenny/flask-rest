from flask import  Flask

app = Flask(__name__)

@app.route("/ping")
def pong():
    return {
        "hello" : "mom!"
    }