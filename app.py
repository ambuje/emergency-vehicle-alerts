import os
from flask import Flask, jsonify,session, redirect, url_for, render_template, abort, request, flash, send_from_directory
from werkzeug.utils import secure_filename
from Waypoints import lat
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def disp():
    orig=request.args['origin']
    dest=request.args['destination']
    checkpnt=request.args['waypoint']
    #print(type(orig))
    orig=orig.split(',')
    orig=list(map(float,orig))
    orig=tuple(orig)
    dest=dest.split(',')
    dest=list(map(float,dest))
    dest=tuple(dest)

    checkpnt=checkpnt.split(',')
    checkpnt=list(map(float,checkpnt))
    checkpnt=tuple(checkpnt)
    print(checkpnt)
    checkpnt=[(item,round(item,4))for item in checkpnt]
    k=lat(orig,dest)
    print(k)
    if checkpnt in k:
        return jsonify(True)
    else:
        return jsonify(False)
if __name__ == '__main__': 
  
    app.run(debug = True,port=5000)
