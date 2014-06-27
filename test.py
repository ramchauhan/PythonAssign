import sys
import unittest
from program import read_data

class TestCsvCode(unittest.TestCase):

    def setUp(self):
        self.file_name = 'test.csv'
        self.input_data1 = {'company': [' A', ' B', ' C', ' D'], 'year': ['1997', '1990', '1991', '1991'], 'price': [' 30', ' 30', ' 30', ' 47'], 'month': [' Oct', ' Jul', ' Aug', ' Aug']}
        self.input_data = {'company': [' A', ' B', ' C', ' D'], 'year': ['1993', '1990', '1991', '1991'], 'price': [' 30', ' 30', ' 30', ' 47'], 'month': [' Oct', ' Jul', ' Aug', ' Aug']}
        
    def test_file(self):
        # for the expected output
        self.assertEqual(self.input_data, read_data(['test.py', self.file_name]))
        # for the not equal
        self.assertNotEqual(self.input_data1, read_data(['test.py', self.file_name]))
        

if __name__ == '__main__':
    unittest.main()   
