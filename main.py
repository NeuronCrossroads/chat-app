from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
  message = "Hello World"
  items = [
    {"icon":"whatshot",
     "header":"Popular",
     "body":"People absolutely love to eat tide pods"},
    {"icon":"directions",
     "header":"Where to go",
     "body":"I don't know"}
  ]
  return render_template("index.html", message=message, items=items)

@socketio.on('add_numbers')
def add_numbers(data):

    emit('added_numbers',{'sum':data['a']+data['b']})

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
    print ('Running')
