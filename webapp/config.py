import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = 'Rostov-on-Don,Russia'
WEATHER_API_KEY = '69455130de1d423eb78130555230412'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')