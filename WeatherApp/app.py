from flask import Flask,render_template,request
from Geocoding import geocoding
from Weather import forecastWeather
from KelvinToCelsius import tocelsius

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        cityname=request.form['search']
        try:
            lat,lon,cityname =geocoding(cityname)
            if lat== None and lon==None:
                return render_template('index.html',error=True)
            weatherdata=forecastWeather(lat,lon)
            weatherdata=tocelsius(weatherdata)
            return render_template('index.html',output=True,weatherData=weatherdata,cityname=cityname)
        except Exception as e:
            return f'OOPS place not found{e}'
    return render_template('index.html',output=False)
        
if __name__=='__main__':
    app.run()
    