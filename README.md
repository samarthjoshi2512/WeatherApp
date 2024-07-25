WeatherApp

Description:

WeatherApp is a Flask-based web application that provides weather information for any location using geolocation and weather data APIs. The app is deployed on PythonAnywhere.

Setup

Clone the repository:

bash

Copy code

git clone https://github.com/yourusername/weatherApp.git

cd weatherApp

Create a virtual environment and activate it:

bash

Copy code

python -m venv venv

source venv/bin/activate # On Windows use venv\Scripts\activate

Install the required packages:

bash

Copy code

pip install -r requirements.txt

Add your API keys:

In Geocoding.py, add your Geoapify API key:

python

Copy code

GEOAPIFY_API_KEY = 'your_geoapify_api_key_here'

In weather.py, add your OpenWeatherMap API key:

python

Copy code

OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key_here'

Run the application locally:

bash

Copy code

flask run

Access the app at http://127.0.0.1:5000.

Deployment on PythonAnywhere

Sign up for a PythonAnywhere account.

Create a new web app and select Flask.

Upload your project files to PythonAnywhere.

Configure the WSGI file to point to your Flask app:

python

Copy code

import sys

import os

path = '/home/yourusername/weatherApp'

if path not in sys.path:

sys.path.append(path)
from app import app as application

Reload your web app on PythonAnywhere.
