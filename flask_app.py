from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "012345ABCDEF"
socket = SocketIO(app)

users = []

@socket.on('connected')
def connect_handle(data):
    print('received json: ' + str(data))
    users.append(data["user"])

@socket.on('disconnecting')
def disconnect_handle(data):
    print('received: ' + str(data))
    users.pop(users.index(data["user"]))

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/view')
def view():
    return str(users)

@app.route("/script/<src>")
def script(src):
    if src == "websockets":
        return render_template("websockets.js")

if __name__ == "__main__":
    socket.run(app)
