from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_signin.html', title="Signin")

@app.route("/", methods=['POST'])
def userform():
    username_error=''
    password_error=''
    verify_error=''
    email_error=''
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    if not username:
        username_error = "Field cannot be empty"
    elif " " in username:
        username_error = "Cannot contain spaces"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Must be between 3 and 20 characters long"

    if not password:
        password_error = "Field cannot be empty"
    elif " " in password:
        password_error = "Cannot contain spaces"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Must be between 3 and 20 characters long"

    if verify != password:
        verify_error = "Passwords do not match"
        password_error = "Passwords do not match"
    elif not verify:
        verify_error = "Field cannot be empty"
    elif " " in verify:
        verify_error = "Cannot contain spaces"
    elif len(verify) < 3 or len(verify) > 20:
        verify_error = "Must be between 3 and 20 characters long"
    
    if not email:
        email_error = ''
    elif len(email) < 3 or len(email) > 20:
        email_error = "Email must be between 3 and 20 characters long"
    elif "@" not in email or "." not in email or " " in email:
        email_error = "Not a valid email"

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('user_signin.html', username=username, username_error=username_error, password_error=password_error, verify_error=verify_error, email=email, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username, title="Welcome")
app.run()