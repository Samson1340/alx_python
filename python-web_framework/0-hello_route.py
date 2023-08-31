from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_HBNB():
    return "<p>Hello HBNB!</p>"