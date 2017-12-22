from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import requests
import os


class GeoLocation(Resource):
    # TODO instruct that they put in spaces for address
    google_base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    geocoder_base_url = 'https://geocoder.cit.api.here.com/6.2/geocode.json?'
    google_api_key = os.environ.get('google_api_key')
    geocoder_app_id = os.environ.get('geocoder_app_id')
    geocoder_app_code = os.environ.get('geocoder_app_code')

    def get_google_service(self, address):
        params = dict(
            address=address,
            key=self.google_api_key
        )
        if self.google_api_key:
            result = requests.get(self.google_base_url, params=params)
            return result
        else:
            raise ValueError('No API key for google api')

    def parse_google_service_lat_lng(self, result):
        return (result['results'][0]['geometry']['location']['lat'],
                result['results'][0]['geometry']['location']['lng'])

    def get_geocoder_service(self, address):
        params = dict(
            searchtext=address,
            app_id=self.geocoder_app_id,
            app_code=self.geocoder_app_code
        )
        if self.geocoder_app_code is not None and self.geocoder_app_id is not None:
            result = requests.get(self.geocoder_base_url, params=params)
            return result
        else:
            raise ValueError('No app id or app code key for geocoder')

    def parse_geocoder_service_lat_lng(self, result):
        return (result['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude'],
                result['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude'])

    def call_services(self, address):
        google_service_result = self.get_google_service(address)
        if google_service_result.status_code == 200:
            lat, lng = self.parse_google_service_lat_lng(google_service_result.json())
            result = {'data': [{'latitude': lat, 'longitude': lng}]}
            return jsonify(result)
        else:
            geocoder_service_result = self.get_geocoder_service(address)
            lat, lng = self.parse_geocoder_service_lat_lng(geocoder_service_result.json())
            result = {'data': [{'latitude': lat, 'longitude': lng}]}
            return jsonify(result)

    def get(self):
        address = request.args.get('address')
        if address:
            return self.call_services(address)
        else:
            result = {'status': 'false', 'message': 'No lat and long given'}
            return result, 400

    def post(self):
        address = request.form.get('address')
        if address:
            return self.call_services(address)
        else:
            result = {'status': 'false', 'message': 'No lat and long given'}
            return result, 400


app = Flask(__name__)
api = Api(app)
api.add_resource(GeoLocation, '/v1/geolocation')

if __name__ == '__main__':
    app.run(port=3000)
