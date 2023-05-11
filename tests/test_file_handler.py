import unittest
import os
import json
from app.utils.file_handler import ssim_to_json, save_json_data
from app.utils.ssim_parser import read_ssim, read_airport_data
from app.utils.filters import filter_by_country_and_service_type

class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.airport_data = read_airport_data('data/airport_data.pkl')
        self.ssim_data = read_ssim('data/EY_SSIM.ssim', self.airport_data)
        self.filtered_data = filter_by_country_and_service_type(self.ssim_data['IT'], 'IT', 'J')
        self.json_data = ssim_to_json(self.filtered_data)
        self.output_file = 'tests/test_output.json'

    def test_ssim_to_json(self):
        self.assertIsNotNone(self.json_data, "Json data should not be None")
        self.assertIsInstance(self.json_data, list, "Json data should be a list")
        self.assertGreater(len(self.json_data), 0, "Json data should not be empty")

    def test_save_json_data(self):
        save_json_data(self.json_data, self.output_file)
        self.assertTrue(os.path.exists(self.output_file), "Output file should be created")

        with open(self.output_file, 'r') as file:
            loaded_json_data = json.load(file)

        self.assertIsInstance(loaded_json_data, list, "Loaded data should be a list")
        self.assertEqual(len(self.json_data), len(loaded_json_data), "Loaded data should have the same length as saved data")

        os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()
