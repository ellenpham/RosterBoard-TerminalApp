import unittest

from Item import Item
from Roster import Roster

# Test the Item class
class TestItem (unittest.TestCase):
    
    # Test the from_str function
    def test_from_string(self):
        input = ["Fri 05/05/2023", "AM", "Added"]
        item = Item.from_str(input)
        self.assertEqual(str(item), "2023-05-05, AM, Added")
        

# Test the class Roster
class TestRoster(unittest.TestCase):
    
    #Test the load_from_file function
    def test_load_from_file(self):
        roster = Roster()
        roster.load_from_file(file_name='test_schedule_record.csv')
        self.assertEqual(len(roster.roster), 3)        

# Main test 
if __name__ == '__main__' :
    unittest.main

