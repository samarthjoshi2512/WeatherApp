import requests

def geocoding(cityname):
    geourl=f'https://api.geoapify.com/v1/geocode/search?text={cityname}&apiKey=a78e93e576bc4c3ab690dd40a01693b8'
    georesponse=requests.get(geourl).json()
    try:
        lat=georesponse["features"][0]["properties"]['lat']
        lon=georesponse["features"][0]["properties"]['lon']
        cityname=georesponse['features'][0]['properties']['name']
    except:
        return None,None,None
    return lat,lon,cityname
    