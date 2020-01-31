import os
from flask import Flask, jsonify,session, redirect, url_for, render_template, abort, request, flash, send_from_directory
from werkzeug.utils import secure_filename
from Waypoints import lat
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAZQl0TRenJIoCbKNjDKmT2LN9Y94um9qs') 
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
    print("checkpnt1",checkpnt)
    p=round(checkpnt[0],3)
    l=round(checkpnt[1],3)
    checkpnt=(p,l)
    print('checkpntt',checkpnt)
    k=lat(orig,dest)
   # print(k)
    if checkpnt in k:
        my_dist = gmaps.distance_matrix(orig,checkpnt)['rows'][0]['elements'][0]
        destt=my_dist['distance']['text']
        destt=destt.split(" ")
        destt=float(destt[0])
        print(destt)
        if destt<=2:
            return jsonify(True)
        else:
            return jsonify(False)
    else:
        return jsonify(False)
if __name__ == '__main__': 
  
    app.run(debug = True,port=5000)
