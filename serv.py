from flask import Flask, render_template, send_from_directory
import os
from threading import Thread
import sys

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

@app.route('/roloo')
def roloo():
  return '	<meta http-equiv="refresh" content="0; url = https://repl.it/join/hmzabkpp-daguacaplushy" />'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/apple-touch-icon.png')
def appletouchicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'apple-touch-icon.png', mimetype='image/png')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def run():
    app.run(host="0.0.0.0", port=5275)    

def serveron():
    site = Thread(target=run)
    site.start()