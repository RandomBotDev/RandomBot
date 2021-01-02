from flask import Flask, render_template, send_from_directory, request, Response
import os
from threading import Thread
from functools import wraps


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'RBAdmin' and password == 'RBDev7'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

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

@app.route('/perms-invite', methods=['GET', 'POST'])
def permsInvite():
  try:
    if request.method == "POST": 
      permsint = request.form.get("perms")
      permsint = int(permsint)
      return f'<meta http-equiv="refresh" content="0; url = https://discord.com/oauth2/authorize?client_id=716309071854174268&permissions={permsint}&redirect_uri=https%3A%2F%2Frandombot.tk%2Fsuccess&scope=bot&response_type=code" /><p>Redirecting you to the invite page.</p>'
  except Exception as e:
    if isinstance(e, ValueError):
      return "You need a valid number..."
  return Response(render_template("404.html"),404)

@app.route('/success')
def success():
  return f'<meta http-equiv="refresh" content="0; url = https://randombot.tk" />'

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