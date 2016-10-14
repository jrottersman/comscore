import unittest

import importer

class TestSchemaMethods(unittest.TestCase):

    def test_length_enforcer_to_long(self):

        newstring = 'a'*65
        
        with self.assertRaises(RuntimeError):
            self.obj = importer.Schema(newstring, newstring, newstring, '2014-04-02', '14.50', '02:15')
    
    def test_null_length_enforcer_empty_string(self):

        with self.assertRaises(RuntimeError):
            self.obj = importer.Schema('','a','a','2014-04-02', '14.50', '02:15')

    def test_date_enforcer_not_year_month_day(self):
        
        with self.assertRaises(RuntimeError):
            self.obj = importer.Schema('a','a','a','02-04-2014', '14.50', '02:15')
    def test_date_enforcer_null(self):
        
        with self.assertRaises(RuntimeError):
            self.obj = importer.Schema('a','a','a','', '14.50', '02:15')

    def test_rev_enforcer_short(self):

        with self.assertRaises(RuntimeError):
            self.obj = importer.Schema('a','a','a','2016-04-02', '14.5', '02:15')
            
    def test_rev_enforcer_letter(self):

        with self.assertRaises(RuntimeError):
            self.obj = importer.Schema('a','a','a','2016-04-02', 'a14.50', '02:15')
    
    def test_time_enforcer_malformed(self):

        with self.assertRaises(RuntimeError):
            self.obj = importer.Schema('a', 'a', 'a', '2016-04-02', '14.50', '1000')

if __name__ == '__main__':
    unittest.main()
