
import threading
from flask_cors import CORS, cross_origin
from flask import jsonify, current_app, render_template
import io
import logging
import socketserver
from http import server
import urllib.parse
from flask import Flask
from flask import request
from time import sleep
import json

app = Flask(__name__)

cors = CORS(app, resources={r'/*':{"origins":'*'}})

data = {'data':{}}

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/sendData',methods=["POST"]) 
def sendData():
    global data
    for key, value in request.form.items():
     data[key] = value
    print(data)
    return 'hi'


@app.route('/getData',methods=["GET"]) 
def getData():
    global data
    return(json.dumps(data))
    
if __name__ =='__main__':
 app.run(host='0.0.0.0',port=80)


 
