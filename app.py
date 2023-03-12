from flask import Flask, render_template, request
import random
import db

app = Flask(__name__)
db.create_db()
@app.route('/')
def mainpage():  # put application's code here
    return render_template("index.html")

@app.route('/signin')
def signin():
    return render_template("index.html")

@app.route('/signup')
def signupPage():
    return render_template("signup.html")

@app.route('/deleteuser')
def deleteUser():
    return render_template("delete.html")

@app.route("/user/add", methods=['POST'])
def add_user():
    username = request.values.get("username")
    password = request.values.get("password")
    yeargroup = request.values.get("yeargroup")
    if db.create_user(username, password, yeargroup):
        return "<h1>successful addition</h1> <button onClick='history.back()'>back</button>"
    else:
        return"Username already taken\n <button onClick='history.back()'>back</button>"

@app.route("/user/login", methods=['POST'])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    if db.login(username,password):
        return render_template("welcome.html")
    else:
        return "Please check your username and password and try again"

@app.route('/test/<string:test>', methods = ['GET', "POST"])
def hi(test = "noname"):
    return "hello, "+str(test)

if __name__ == "__main__":
    db.create_db()
    print("hello")
    app.run(host="0.0.0.0", port=81, debug = True)
