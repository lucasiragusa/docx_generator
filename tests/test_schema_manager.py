import unittest
import json
from app.utils.schema_manager import load_json_schema, validate_json_data

class TestSchemaManager(unittest.TestCase):

    def setUp(self):
        self.schema_path = 'schemas/flight_data_schema.json'
        self.schema = load_json_schema(self.schema_path)

        self.valid_data = {
            "Flight_number": "EY123",
            "Service_Type": "J",
            "Eff": "01MAY22",
            "Dis": "31MAY22",
            "Days_of_operation": "1234567",
            "Dept_Stn": "AUH",
            "Dept_time_pax": "1000",
            "Arvl_Stn": "JFK",
            "Arvl_time_pax": "1600",
            "Equipment": "789",
            "Aircraft_configuration": "C12Y270",
            "Departure_country": "AE",
            "Arrival_country": "US"
        }

        self.invalid_data = {
            "Flight_number": "EY123",
            "Service_Type": "J",
            "Eff": "01MAY22",
            "Dis": "31MAY22",
            "Days_of_operation": "1234567",
            "Dept_Stn": "AUH",
            "Dept_time_pax": "1000",
            "Arvl_Stn": "JFK",
            "Arvl_time_pax": "1600",
            "Equipment": "789",
            "Aircraft_configuration": "C12Y270",
            "Departure_country": 123,  # Invalid type
            "Arrival_country": "US"
        }

    def test_load_json_schema(self):
        self.assertIsInstance(self.schema, dict)

    def test_validate_json(self):
        is_valid = validate_json_data(self.valid_data, self.schema)
        self.assertTrue(is_valid)

        is_valid = validate_json_data(self.invalid_data, self.schema)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
