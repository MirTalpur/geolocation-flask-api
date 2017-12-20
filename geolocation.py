from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
# from flask import status
# from flask.ext.api import status

app = Flask(__name__)
api = Api(app)

class GeoLocation(Resource):
    def get(self):
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        if latitude and longitude:
            result = {'data': [{'latitude': latitude, 'longitude': longitude}]}
            return jsonify(result)
        else:
            result = {'status': 'false', 'message': 'No lat and long given'}
            return result,400



api.add_resource(GeoLocation, '/v1/geolocation')

if __name__ == '__main__':
    app.run(port=3000)