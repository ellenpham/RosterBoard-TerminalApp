import datetime

# Define the Item class that represents an item in the roster or unavailability record
# Each item is users' input of each available day with available shift or unavailable days with available shifts
class Item:
    
    # initialize an Item object from input parameters
    def __init__(self, day, shift, action):
        self.day = day
        self.shift = shift
        self.action = action
        
    # initialize an Item object from an input string
    # a class method to create a 
    # Day object by a string of Date(including year, month, day), Shift and Action
    @classmethod
    def from_str(self, str_data):
        try:
            str = str_data[0]
            str = str[4:]
            str = str.split("/")
            date = int(str[0])
            month = int(str[1])
            year = int(str[2])
            day = datetime.date(year,month,date)
            shift = str_data[1]
            action = str_data[2]        
            item = Item(day, shift, action)
            return item
        except ValueError:
            print("invalid_input_message()")
    
    # this is how the item is represented in string    
    def __str__(self):
        return f"{self.day} -  {self.shift} - {self.action}"