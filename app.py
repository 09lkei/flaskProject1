from flask import Flask, render_template, request, redirect, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloworld'
db.create_db()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(username):
    return db.user_details(username)

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
        return"Username already taken or invalid year group (2 characters)\n <button onClick='history.back()'>back</button>"

@app.route("/user/login", methods=['POST'])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    if db.login(username,password):
        return redirect(url_for("dashboard"))
    else:
        return "Please check your username and password and try again"

@app.route("/dashboard", methods = ['GET','POST'])
@login_required
def dashboard():
    return render_template("welcome.html", username=load_user)

if __name__ == "__main__":
    db.create_db()
    print("hello")
    app.run(host="0.0.0.0", port=81, debug = True)
