from flask import Flask
from flask_restful import Api
from geolocation import GeoLocation

app = Flask(__name__)
api = Api(app)
api.add_resource(GeoLocation, '/v1/geolocation')

if __name__ == '__main__':
    app.run(port=3000)
