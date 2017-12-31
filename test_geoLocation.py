from unittest import TestCase
import unittest
from geolocation import GeoLocation

class TestGeoLocation(TestCase):
    address = "1600 Amphitheatre Parkway, Mountain View, CA"

    def test_get_google_service(self):
        geolocation = GeoLocation()
        result = geolocation.get_google_service(self.address)
        self.assertEqual(result.status_code,200)

    def test_parse_google_service_lat_lng(self):
        geolocation = GeoLocation()
        result = geolocation.get_google_service(self.address)
        lat, lng = geolocation.parse_google_service_lat_lng(result.json())
        self.assertAlmostEqual(lat, 37.422,delta=0.1)
        self.assertAlmostEqual(lng, -122.084,delta=0.1)

    def test_get_geocoder_service(self):
        geolocation = GeoLocation()
        result = geolocation.get_geocoder_service(self.address)
        self.assertEqual(result.status_code, 200)

    def test_parse_geocoder_service_lat_lng(self):
        geolocation = GeoLocation()
        result = geolocation.get_geocoder_service(self.address)
        lat, lng = geolocation.parse_geocoder_service_lat_lng(result.json())
        self.assertAlmostEqual(lat, 37.422, delta=0.1)
        self.assertAlmostEqual(lng, -122.084, delta=0.1)

    def test_call_services(self):
        pass

    def test_get(self):
        pass

    def test_post(self):
        pass

if __name__ == '__main__':
    unittest.main()