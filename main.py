from flask import Flask, request, redirect, render_template
import cgi
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



@app.route("/add", methods=['POST'])
def add_info():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form ['verify_password']
    email = request.form ['email']

    # if the user typed nothing at all, redirect and tell them the error

   # """username_error_1 == (len(username) < 1)
   # if username_error_1:
   #     return redirect("/?error=" + username_error_1 )"""

    if (not username) or (username.strip() == ""):
        username_error_1 = "Please add a username."
        return render_template('index.html', username=username, email=email, 
        username_error_1=username_error_1)

    if " " in (username.strip()):
        username_error_2 = "Please do not use spaces in username."
        return render_template('index.html', username=username, email=email, 
        username_error_2=username_error_2)

    if len(username) < 3:
        username_error_3 = "Username must be three characters or more."
        return render_template('index.html', username=username, email=email,
        username_error_3=username_error_3)

    if len(username) > 20:
        username_error_4 = "Username must be less than 20 characters."
        return render_template('index.html', username=username, email=email,
        username_error_4=username_error_4)


 
    if (not password) or (password.strip() == ""):
        password_error_1 = "Please add a password."
        return render_template('index.html', username=username, email=email,
        password_error_1=password_error_1)

    if " " in (password.strip()):
        password_error_3 = "Please do not use spaces in password."
        return render_template('index.html', username=username, email=email,
        password_error_3=password_error_3)

    if len(password) < 3:
        password_error_4 = "Password must be three characters or more."
        return render_template('index.html', username=username, email=email,
        password_error_4=password_error_4)

    if len(password) > 20:
        password_error_5 = "Password must be less than 20 characters."
        return render_template('index.html', username=username, email=email, 
        password_error_5=password_error_5)



    if (not verify_password) or (verify_password.strip() == ""):
        verify_error_1 = "Please verify password."
        return render_template('index.html', username=username, email=email,
        verify_error_1=verify_error_1)

    if (password) != (verify_password):
        verify_error_2 = "Passwords must match."
        return render_template('index.html', username=username, email=email,
        verify_error_2=verify_error_2)



    if (email) and "@" not in (email.strip()): 
        email_error_1 = "Must be a valid email address."
        return render_template('index.html', username=username, email=email, 
        email_error_1=email_error_1)


    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    username_escaped = cgi.escape(username, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    verify_password_escaped = cgi.escape(verify_password, quote=True)
    email_escaped = cgi.escape(email, quote=True)


    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
