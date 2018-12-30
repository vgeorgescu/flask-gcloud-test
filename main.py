import json

from flask import Flask
from flask import render_template
from flask import session

from auth import requires_auth, auth

app = Flask(__name__)
app.secret_key = b'nyUgM0hDK4_rN5N'
app.register_blueprint(auth)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))
