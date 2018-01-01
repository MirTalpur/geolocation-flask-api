from unittest import TestCase
import unittest
from geolocation.geolocation import GeoLocation
import geolocation


class TestGeoLocation(TestCase):
    address = "1600 Amphitheatre Parkway, Mountain View, CA"

    def setUp(self):
        geolocation.app.testing = True
        self.app = geolocation.app.test_client()

    def test_get_google_service(self):
        geo_location = GeoLocation()
        result = geo_location.get_google_service(self.address)
        self.assertEqual(result.status_code, 200)

    def test_parse_google_service_lat_lng(self):
        geo_location = GeoLocation()
        result = geo_location.get_google_service(self.address)
        lat, lng = geo_location.parse_google_service_lat_lng(result.json())
        self.assertAlmostEqual(lat, 37.422, delta=0.1)
        self.assertAlmostEqual(lng, -122.084, delta=0.1)

    def test_get_geocoder_service(self):
        geo_location = GeoLocation()
        result = geo_location.get_geocoder_service(self.address)
        self.assertEqual(result.status_code, 200)

    def test_parse_geocoder_service_lat_lng(self):
        geo_location = GeoLocation()
        result = geo_location.get_geocoder_service(self.address)
        lat, lng = geo_location.parse_geocoder_service_lat_lng(result.json())
        self.assertAlmostEqual(lat, 37.422, delta=0.1)
        self.assertAlmostEqual(lng, -122.084, delta=0.1)

    def test_get(self):
        query_param = {
            'address': self.address,
        }
        result = self.app.get('/v1/geolocation', query_string=query_param)
        assert 'latitude' in result.data
        assert 'longitude' in result.data

    def test_post(self):
        post_data = dict(
            address=self.address,
        )
        result = self.app.post('/v1/geolocation', data=post_data)
        assert 'latitude' in result.data
        assert 'longitude' in result.data


if __name__ == '__main__':
    unittest.main()
