from flask import Flask
from myapp import auth, main

app = Flask(__name__)
app.secret_key = b'nyUgM0hDK4_rN5N'
app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)