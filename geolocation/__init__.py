from flask import Flask
from flask_restful import Api
from geolocation import GeoLocation

app = Flask(__name__)
api = Api(app)
api.add_resource(GeoLocation, '/v1/geolocation')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
