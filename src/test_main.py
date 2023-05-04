# unit test case
import unittest

from Item import Item
from Roster import Roster
from main import input_name, department_choice
from common_functions import check_valid_shift

# Test valid shift input
class TestValidShift(unittest.TestCase):
    def test_check_valid_shift(self):
        test_shift_1 = "AM"
        test_shift_2 = "PM"
        test_shift_3 = "Night"
        self.assertTrue(check_valid_shift(test_shift_1))
        self.assertTrue(check_valid_shift(test_shift_2))
        self.assertTrue(check_valid_shift(test_shift_3))

# Test invalid shift input
class TestInvalidShift(unittest.TestCase):
    def test_check_valid_shift(self):
        test_shift_1 = "am"
        test_shift_2 = "!#$"
        test_shift_3 = "123"
        self.assertFalse(check_valid_shift(test_shift_1))
        self.assertFalse(check_valid_shift(test_shift_2))
        self.assertFalse(check_valid_shift(test_shift_3))

# Test the Item class
class TestItem (unittest.TestCase):
    """
    Test if the from_str() method works as expected:
    Check if item object are the same despite different date format 
    """
    def test_from_string(self):
        input = ["Fri 05/05/2023", "AM", "Added"]
        item = Item.from_str(input)
        self.assertEqual(str(item), "2023-05-05, AM, Added")
        

# Test the class Roster
class TestRoster(unittest.TestCase):
    """
    Test if the load_from_file() method works as expected.
    The number of item from csv file and number of item loaded to the roster list is the same.
    """
    def test_load_from_file(self):
        roster = Roster()
        roster.load_from_file(file_name='test_schedule_record.csv')
        self.assertEqual(len(roster.roster), 3)        

# Main test 
if __name__ == '__main__' :
    unittest.main()

