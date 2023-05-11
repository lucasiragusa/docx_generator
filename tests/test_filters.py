import unittest
import pandas as pd
from app.utils.ssim_parser import read_airport_data, read_ssim
from app.utils.filters import filter_by_country, filter_by_service_type

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.airport_data = read_airport_data('data/airport_data.pkl')
        self.ssim_data = read_ssim('data/EY_SSIM.ssim', self.airport_data)

    def test_filter_by_country(self):
        country_code = 'IT'
        filtered_data = filter_by_country(self.ssim_data, country_code)

        for key, df in filtered_data.items():
            self.assertTrue(((df['Departure_country'] == country_code) | (df['Arrival_country'] == country_code)).all())

    def test_filter_by_service_type(self):
        service_type = 'J'
        filtered_data = filter_by_service_type(self.ssim_data, service_type)

        for key, df in filtered_data.items():
            self.assertTrue((df['Service Type'] == service_type).all())

if __name__ == '__main__':
    unittest.main()
