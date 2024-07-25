import requests

def geocoding(cityname):
    geourl=f'https://api.geoapify.com/v1/geocode/search?text={cityname}&apiKey=ADD YOUR API KEY'
    georesponse=requests.get(geourl).json()
    try:
        lat=georesponse["features"][0]["properties"]['lat']
        lon=georesponse["features"][0]["properties"]['lon']
        cityname=georesponse['features'][0]['properties']['name']
    except:
        return None,None,None
    return lat,lon,cityname
    
