from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/') 
def home():
    return "Ma création vivra"

def run():
    app.run(host='0.0.0.0', port=8080)

def Bluntimer_Keep_Alive():
    t = Thread(target=run)
    t.start()