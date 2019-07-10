import requests
import json
import math
Key = 'AIzaSyAq0dLp59Cpk6deLTQpeluwMIwo3xrW_B0'
#Store google maps api url in a variable
#url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
# call get method of request module and store respose object
#r = requests.get(url + 'origins=' + 'pune' + '&destinations=' + 'mumbai' + '&key=' + apiKey)
#Get json format result from the above response object
#res = r.json()
#print the value of res
#distance = res['rows'][0]['elements'][0]['distance']['value']
def getLocs(apiKey):
    lats=[]
    longs=[]
    distance=[]
    url2='https://maps.googleapis.com/maps/api/directions/json?'
    r2 = requests.get(url2 + 'origin=' +'pune' + '&destination=' +'mumbai' + '&key=' + apiKey)
    res2=r2.json()
    for i in range(37):
        lats.append(res2['routes'][0]['legs'][0]['steps'][i]['end_location']['lat'])
        longs.append(res2['routes'][0]['legs'][0]['steps'][i]['end_location']['lng'])
    return lats, longs
#getLocs(Key)
def getWind():
    lats, long = getLocs(Key)
    url3='http://samples.openweathermap.org/data/2.5/weather?'
    r3=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Mumbai,india&APPID=ac88672e8521b223ccb73d01206cee19')
    res3=r3.json()
    return res3['wind']['speed']
#getWind()
def getTheta(apiKey):
    c=[]
    lats, longs = getLocs(Key)
    url3='https://maps.googleapis.com/maps/api/elevation/json?'
    for i,j in zip(lats,longs):
        #print(str(i) +',' +str(j))
        r3=requests.get(url3 + 'locations=' + str(i) +',' +str(j) +'&key='+apiKey)
        #print(url3 + 'locations=' + str(i) +',' +str(j) +'&key='+apiKey)
        res3=r3.json()
        a =res3['results'][0]['elevation']
        b = res3['results'][0]['resolution']
        c.append(math.radians(math.atan(a/b)))
    #print(math.degrees(math.atan(a/b)))
    return c
#getTheta(Key)
def getSpeed(apiKey):
        lats, longs = getLocs(Key)
        s=""
        print(lats, longs)
        for i,j in zip(lats,longs):
                s=s+str(i)+","+str(j)+"|"
        print(s)
        url3='https://roads.googleapis.com/v1/speedLimits?path='
        r3=requests.get(url3 + s + '&key='+apiKey)
        res3=r3.json()
#getSpeed()


def Power_Required(wind_speed,velocity, cos_theta, sin_theta, acceleration):  # V is driving speed
        
        mass = 2000 #kg
        mass_factor = 1.05
        coeff_roll_R = 0.02  # coefficient of rolling resistance
        air_density = 1.225 # kg/m^3
        front_area = 2 # m^2
        aero_drag_coff = 0.5
        road_angle = 0 # angle

        p1 = (mass_factor * mass * acceleration) + (mass * 9.8 * coeff_roll_R * cos_theta)
        p2 = 0.5 * air_density * front_area * aero_drag_coff * ((velocity - wind_speed)**2)
        p3 = mass * 9.8 * sin_theta

        P_req = 0.001*(p1 + p2 + p3) * velocity   # Watt
        return P_req

angle_array=getTheta(Key)
print(angle_array)
w_speed=getWind()
#print(w_speed)
#p=0
#for i in range(37):
#        power=Power_Required(w_speed,12,math.cos(angle_array[i]),math.sin(angle_array[i]), 10)
#        p+=power
#print(p)
        