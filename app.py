from flask import Flask, render_template, request
import random
import db

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/signup')
def signupPage():
    return render_template("signup.html")

@app.route("/user/add", methods=['POST'])
def add_user():
    email = request.values.get("email")
    password = request.values.get("password")
    if db.create_user(email,password):
        return "<h1>successful addition</h1> <button onClick='history.back()'>back</button>"
    else:
        return"unsuccessful addition <button onClick='history.back()'>back</button>"



@app.route('/test/<string:test>', methods = ['GET', "POST"])
def hi(test = "noname"):
    return "hello, "+str(test)

if __name__ == "__main__":
    db.create_db()
    print("hello")
    app.run(host="0.0.0.0", port=81, debug = True)
