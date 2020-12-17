from flask import Flask, render_template
from threading import Thread

app = Flask('RandomBot')

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/invite')
def invite():
    return render_template("invite.html")

@app.route('/support')
def support():
    return render_template("support.html")

def run():
    app.run(host="0.0.0.0", port=4573)    

def serveron():
    site = Thread(target=run)
    site.start()