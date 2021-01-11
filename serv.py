from flask import Flask, render_template, send_from_directory, request, Response
import os
from threading import Thread
import requests
app = Flask('RandomBot')

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "base-uri 'self'"
    return response

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
      return Response(render_template("permsinput.html"),200)
    elif request.method == "GET":
      try:
        perms = request.args.get('perms')
        perms = int(perms)
        return f'<meta http-equiv="refresh" content="0; url = https://discord.com/oauth2/authorize?client_id=716309071854174268&permissions={perms}&redirect_uri=https%3A%2F%2Frandombot.tk%2Fsuccess&scope=bot&response_type=code" /><p>Redirecting you to the invite page.</p>'
        return Response(render_template("permsinput.html"),200)
      except:
        return Response('You need a valid permission integer query string. Try https://randombot.tk/pers-invite?perms=(permissions integer)',500)
  except Exception as e:
    if isinstance(e, ValueError):
      return "You need a valid number..."

@app.route('/success')
def success():
  return f'<meta http-equiv="refresh" content="0; url = https://randombot.tk" />'

@app.route('/raid-notify')
def raidnotify():
  return render_template("rickroll.html")


@app.route('/500')
def fivezerozero():
  return Response(render_template("errors/500.html"),500)

@app.route('/redir')
def redir():
  url = request.args.get('url')
  urlr = requests.get(f"{url}")
  return f'''<meta http-equiv="refresh" content="0; url = {url}" /><div style="visibility:hidden">{urlr.text}</div>'''

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt', mimetype='text/plain')

@app.route('/apple-touch-icon.png')
def appletouchicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'apple-touch-icon.png', mimetype='image/png')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def app_error(e):
    return render_template('errors/500.html'), 500

def run():
    app.run(host="0.0.0.0", port=5275)    

def serveron():
    site = Thread(target=run)
    site.start()