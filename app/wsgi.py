from flask import Flask, render_template
from flask_socketio  import SocketIO, send
import socket

app = Flask(__name__)
app.config['SECRET'] ='SCE455@333434334'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print("received message"+message)
    if message != "User connected!":
        send(message,broadcast=True)

@app.route('/')
def index():
    render_template("index.html")

@app.route('/test')
def hello():    
    return f"container id: {socket.gethostname()}" #this is will return container id as hostname

if __name__ == "__main__":
    socketio.run(app, host="localhost",debug=True)