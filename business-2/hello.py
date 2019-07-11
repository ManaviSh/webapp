from flask import Flask, render_template, request
from main import getData
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', active='home')
@app.route('/map' , methods=['post', 'get'])
def map():
   formData = {
      "origin": None,
      "destination": None,
      "soc": None,
   }
   returnData = {}
   if request.method == 'POST':
        formData['origin'] = request.form.get('origin')  # access the data inside 
        formData['destination'] = request.form.get('destination')
        formData['soc'] = request.form.get('soc')
        returnData = getData(formData['origin'], formData['destination'], formData['soc'])
   return render_template('map.html', active='map', data=formData, returnData=returnData)

if __name__ == '__main__':
   app.run(debug = True)