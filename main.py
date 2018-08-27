from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

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

@app.route('/add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    print (request)
    return jsonify(result=a + b)

if __name__ == "__main__":
	#decide what port to run the app in
	port = 8080
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)
