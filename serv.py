from flask import Flask, render_template, send_from_directory, request, Response
import os
from threading import Thread
import requests
from base64 import b64decode as b64d
import json

app = Flask('RandomBot')

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "base-uri 'self'"
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
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

@app.route('/cf504')
def cf504():
    return render_template("errors/cf504.html")

@app.route('/claim_KLUWudK7Zb2rm3A/', methods=['POST'])
def claim_KLUWudK7Zb2rm3A():
  user = request.form.get('username')
  g = False
  r = []
  for x in range(1, 10000):
    r.append(user.endswith(str(x)))
  for d in r:
    if d == True:
      g = True
  if g == False or not '#' in user:
    return '<center><p>Thats not a username!</p></center>'
  global KLUWudK7Zb2rm3A_claimed
  KLUWudK7Zb2rm3A_claimed = True
  print("{} claimed KLUWudK7Zb2rm3A!".format(user))
  return '<meta http-equiv="refresh" content="0; url = https://randombot.tk//claimed_KLUWudK7Zb2rm3A/" />'

@app.route('/claimed_KLUWudK7Zb2rm3A/')
def claimed_KLUWudK7Zb2rm3A():
  try:
    if KLUWudK7Zb2rm3A_claimed:
      return "<center><p>Gift claimed!</p></center>"
      '''return \'''<style> #vid-blocker {
                  position:absolute;
                  top: 0px;
                  left: 0px;
                  height: 100%;
                  width: 100%;
                  z-index: 5;
              }</style><center><div id="vid-blocker"></div><iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1" width="100%" height="100%" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></center>'''
    else:
      return "<center><p>Not claimed yet! https://randombot.tk/gift/KLUWudK7Zb2rm3A</p></center>"
  except:
    return "<center><p>Not claimed yet! https://randombot.tk/gift/KLUWudK7Zb2rm3A</p></center>"

@app.route('/gift/KLUWudK7Zb2rm3A')
def KLUWudK7Zb2rm3A():
  try:
    if KLUWudK7Zb2rm3A_claimed:
      return "<center><p>Gift already claimed!</p></center>"
    else:
      return render_template("gift/KLUWudK7Zb2rm3A.html")
  except NameError:
    return render_template("gift/KLUWudK7Zb2rm3A.html")

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
        return Response('You need a valid permission integer query string. Try https://randombot.tk/pers-invite?perms=(permissions integer)', 200)
  except Exception as e:
    if isinstance(e, ValueError):
      return Response("You need a valid number...", 400)

@app.route('/success')
def success():
  return '<meta http-equiv="refresh" content="0; url = https://randombot.tk" />'

@app.route('/raid-notify')
def raidnotify():
  return render_template("rickroll.html")

@app.route('/500')
def fivezerozero():
  return Response(render_template("errors/500.html"),500)

@app.route('/redir')
def redir():
  if request.args.get('base64'):
    url = b64d(request.args.get('url')).decode()
  else:
    url = request.args.get('url')
  try:
    urlr = requests.get(f"{url}").text
  except Exception as e:
    if str(e).startswith("Invalid URL"):
      urlr = "<center><p>Thats not a URL!</p></center>"
  return f'''<meta http-equiv="refresh" content="0; url = {url}" /><div style="visibility:hidden">{urlr}</div>'''

@app.route('/render')
def render():
  cnt = str(request.args.get("html"))
  return f'{cnt}'

@app.route('/topgg', methods=["POST"])
def topgg():
  if request.headers["Authorization"] == "randombot_vote_key_7163":
    pass
  else:
    return Response("", 401)
  user = request.json
  mainuser = json.loads(requests.get(f'https://discord.com/api/v8/users/{user["user"]}', headers = {"Authorization": f'Bot {os.getenv("auth_token")}'}).content)
  mainbot = json.loads(requests.get(f'https://discord.com/api/v8/users/{user["bot"]}', headers = {"Authorization": f'Bot {os.getenv("auth_token")}'}).content)
  try:
    if user["type"] == "test":
      voteinfo = f'{mainuser["username"]}#{mainuser["discriminator"]} just test voted for {mainbot["username"]}#{mainbot["discriminator"]}!'
    else:
      voteinfo = f'{mainuser["username"]}#{mainuser["discriminator"]} just voted for {mainbot["username"]}#{mainbot["discriminator"]}!'
  except KeyError:
    voteinfo = f'{mainuser["username"]}#{mainuser["discriminator"]} just voted for {mainbot["username"]}#{mainbot["discriminator"]}!'
  requests.post('https://discord.com/api/webhooks/809867547029274704/1LdTWK79vyUYhIs4FZqK-Ts1pDPl8t71gu7jmNWkZv1nIRzdqCkXH4HsT0RcJSOYCIiX', json={"content": voteinfo})
  return "Success!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/mirawobble.gif')
def mirawobble():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'mirawobble.gif', mimetype='image/gif')

@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt', mimetype='text/plain')

@app.route('/apple-touch-icon.png')
def appletouchicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'apple-touch-icon.png', mimetype='image/png')

@app.route('/pecala.png')
def pecala():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'pecala.png', mimetype='image/png')

@app.route('/manifest.json')
def manifest():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'manifest.json', mimetype='application/json')

@app.route('/sw.js')
def sw():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sw.js', mimetype='text/javascript')

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