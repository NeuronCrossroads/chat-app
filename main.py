from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
  message = "Group-arpan Chatt"
  return render_template("index.html", message=message)

@socketio.on('connecting')
def connect(data):
    emit('broadcast',{'text':'Connected'})

@socketio.on('send_message')
def send_message(data):
    message = data['text']
    emit('broadcast',{'text':message},broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080)
    print ('Running')
