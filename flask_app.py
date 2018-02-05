from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "012345ABCDEF"
socket = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/script/<script_name>")
def script(src):
    if src == "websockets":
        return render_template("websockets.js")

if __name__ == "__main__":
    socket.run(app)
