from flask import Flask, render_template, request
# export FLASK_APP=/home/mainuser/scripts/Lookback/server.py


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html") 

@app.route("/info")
def info():
	return render_template("info.html")

@app.route("/test")
def test():
	name = request.args.get("name", "User, try putting ?name=<yourname> in the url")
	return render_template("test.html", test=name)

@app.route("/search", methods=["POST"])
def search():
	search = request.form.get("search")
	catagory = request.form.get("type")
	print (search)
	print (catagory)
	if not search or not catagory:
		return"400 - Bad Request: Try giving an input"
	return render_template("search.html", search=search, catagory=catagory)
