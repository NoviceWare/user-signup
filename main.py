from flask import Flask, request, redirect, render_template, flash
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def check_string(string):
    if string.find(" ") != -1 or len(string) < 3 or len(string) > 20:
        return False
    else:
        return True

def check_email(string):
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

#@app.route("/welcome", methods=['GET', 'POST'])
#def welcome(login):
#    return render_template("welcome.html", login=login)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login = request.form['login']
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        #Verify login
        if login:
            if check_string(login) == False:
                flash('login reqs: alphanumeric and between 3-20 characters', 'loginerror')
                return render_template('base.html')
        else:
            flash('login is required', 'loginerror')
            return render_template('base.html')

        # Verify passwords
        if password and verify:
            if password != verify:
                flash('passwords did not match', 'passworderror')
                return render_template('base.html')
            else:
                if check_string(password) == False:
                    flash('password reqs: alphanumeric and between 3-20 characters', 'passworderror')
                    return render_template('base.html')
        else:
            flash('password and verification is required', 'passworderror')
            return render_template('base.html')

        # Verify email if it exists
        if email:
            if check_email(email) == False:
                flash(email + ' is not a valid email address', 'emailerror')
                return render_template('base.html')

        return render_template('welcome.html', login=login)
    else:
        return render_template('base.html')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == "__main__":
    app.run()
