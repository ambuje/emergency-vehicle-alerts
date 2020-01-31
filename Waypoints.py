import googlemaps
from datetime import datetime
import polyline
def lat(a,b):
    gmaps = googlemaps.Client(key='AIzaSyAZQl0TRenJIoCbKNjDKmT2LN9Y94um9qs')
    now = datetime.now()
    directions_result = gmaps.directions(a, b,
                                         mode="driving",
                                         departure_time=now)
    final=list()
    for i in directions_result:
        #print(i.keys())
       # print(i['legs'])
        for j in i['legs']:
            #print(j.keys())
            for k in j['steps']:
               # print(k['polyline'])
                final.append(k['polyline'])
    
    finall=[]
    for p in final:
        #print(p)
        #print(p['points'])
        finall.extend(polyline.decode(p['points']))
    finall=[(round(item[0],3),round(item[1],3))for item in finall]
    #print((finall))
    #print(len(finall))
    return finall
