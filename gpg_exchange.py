from flask import Flask, render_template
GPG_EXCHANGE = Flask(__name__)

@GPG_EXCHANGE.route('/')
def home():
    return render_template("home.html")