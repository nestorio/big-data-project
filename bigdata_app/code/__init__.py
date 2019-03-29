from flask import Flask, render_template, url_for, request, session, redirect
import pymongo
import bcrypt
app = Flask(__name__)

#This is the route that leads to the index page
@app.route('/')
def index():
    if('username' in session):
        return "You are logged in as" + session['username']
    return render_template('index.html')

# This is the login route which links to the login page
@app.route('/login')
def login():
    return render_template('login.html')

# This is the registration route which lead to the registration page
@app.route('/register')
def register():
    return render_template('sign-up.html')

if __name__ == '__main__':
    app.run(debug=True)