from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    if message != "User connected!":
        send(message, broadcast=True)
        #with broadcast=True, all clients connected can see the message


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    #if you want to connect other clients to this server, replace 'localhost' with your ip address
    socketio.run(app, host="localhost")
