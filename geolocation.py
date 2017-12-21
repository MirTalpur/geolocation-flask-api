from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import requests
import os
# from flask import status
# from flask.ext.api import status

app = Flask(__name__)
api = Api(app)

class GeoLocation(Resource):
    # TODO change request type to POST Instead
    def get_google_service(self, address):
        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        api_key = os.environ.get('google_api_key')
        params = dict(
            address=address,
            key=api_key
        )
        if api_key:
            # url = base_url + 'address=' + address + '&key=' + api_key
            result = requests.get(base_url,params=params)
            return result
        else:
            raise ValueError('No API key for google api')

    def parse_for_lat_lng(self, result):
        return (result['results'][0]['geometry']['location']['lat'],
                result['results'][0]['geometry']['location']['lng'])

    def get(self):
        address = request.args.get('address')
        if address:
            google_service_result = self.get_google_service(address)
            print google_service_result
            if google_service_result.status_code == 200:
                lat,lng = self.parse_for_lat_lng(google_service_result.json())
                result = {'data':[{'latitude': lat, 'longitude':lng}]}
                return jsonify(result)
            else:
                print 'Other serivce'
                # use another service
            # return jsonify(result)
        else:
            result = {'status': 'false', 'message': 'No lat and long given'}
            return result,400



api.add_resource(GeoLocation, '/v1/geolocation')

if __name__ == '__main__':
    app.run(port=3000)