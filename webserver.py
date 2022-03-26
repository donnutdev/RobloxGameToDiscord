import requests
from flask import Flask, request
from replit import db
from module import verification_requests, bot
from threading import Thread

app = Flask(__name__)


@app.route('/')
def index():
  return "I'm alive!"


@app.route('/verify/playerjoined/<robloxid>', methods=['GET'])
def verification_(robloxid):
  v = verification_requests.get(int(robloxid), False)
  if v == False:
    return {'success':False}
  else:
    return v

@app.route('/verify/verified', methods=['POST'])
def verified():
  if request.method == 'POST':
    db[request.json['robloxId']] = verification_requests[request.json['robloxId']]['discordId']
    del verification_requests[request.json['robloxId']]
    print(verification_requests)
    return 'Success'

def run():
  app.run(host='0.0.0.0',port=8080)


def keep_alive():  
    t = Thread(target=run)
    t.start()