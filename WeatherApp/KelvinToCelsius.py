def tocelsius(weatherData):
    weatherData['temperature']=round(weatherData['temperature']-273.15)
    weatherData['temp_min']=round(weatherData['temp_min']-273.15)
    weatherData['temp_max']=round(weatherData['temp_max']-273.15)
    return weatherData 