import os
import unittest
import pandas as pd
from app.utils.permit_generator import create_permit_document, save_permit_document

class TestPermitGenerator(unittest.TestCase):

    def setUp(self):
        self.regulator = "Regulator"
        self.airline = "Airline"
        self.representative_name = "John Doe"
        self.start_date = "2023-03-01"
        self.end_date = "2023-03-31"

        self.df = pd.DataFrame(
            [
                ["EY123", "J", "01MAY22", "31MAY22", "1234567", "AUH", "1000", "JFK", "1600", "789", "C12Y270", "AE", "US"],
                ["EY124", "J", "01MAY22", "31MAY22", "1234567", "JFK", "1800", "AUH", "0800", "789", "C12Y270", "US", "AE"],
            ],
            columns=[
                "Flight_number",
                "Service_Type",
                "Eff",
                "Dis",
                "Days_of_operation",
                "Dept_Stn",
                "Dept_time_pax",
                "Arvl_Stn",
                "Arvl_time_pax",
                "Equipment",
                "Aircraft_configuration",
                "Departure_country",
                "Arrival_country",
            ],
        )

        self.output_file = "test_permit_document.docx"

    def test_permit_generator(self):
        document = create_permit_document(self.regulator, self.airline, self.representative_name, self.start_date, self.end_date, self.df)
        save_permit_document(document, self.output_file)

        self.assertTrue(os.path.exists(self.output_file))

    # def tearDown(self):
    #     if os.path.exists(self.output_file):
    #         os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()
