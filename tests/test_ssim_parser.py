import unittest
import pandas as pd
import os
from app.utils.ssim_parser import read_airport_data, read_ssim

class TestSSIMParser(unittest.TestCase):

    def setUp(self):
        self.airport_data = read_airport_data('data/airport_data.pkl')
        self.ssim_data = read_ssim('data/EY_SSIM.ssim', self.airport_data)

    def test_read_ssim_output_type(self):
        # Check if the output is a dictionary
        self.assertIsInstance(self.ssim_data, dict)

    def test_read_ssim_dataframe_not_empty(self):
        # Check if the dataframes in the output dictionary are not empty
        for country, df in self.ssim_data.items():
            self.assertFalse(df.empty)

    def test_read_ssim_columns(self):
        # Check if the resulting DataFrames have the expected columns
        expected_columns = [
            'Flight number', 'Service Type', 'Eff', 'Dis',
            'Day(s) of operation', 'Dept Stn', 'Dept time (pax)',
            'Arvl Stn', 'Arvl time (pax)', 'Equipment',
            'Aircraft configuration', 'Departure_country', 'Arrival_country'
        ]
        for country, df in self.ssim_data.items():
            self.assertTrue(set(expected_columns).issubset(df.columns))

if __name__ == '__main__':
    unittest.main()
