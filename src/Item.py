import datetime

#define the Item class that represent an item in the rosters
class Item:
    
    # initialize an Item object from input paramerters
    def __init__(self, date, shift, action):
        self.date = date
        self.shift = shift
        self.action = action
        
    # initialize an Item object from an input string
    @classmethod
    def from_str(self, str_data):
        try:
            str = str_data[0]
            str = str[4:]
            str = str.split("/")
            day = int(str[0])
            month = int(str[1])
            year = int(str[2])
            date = datetime.date(year,month,day)
            shift = str_data[1]
            action = str_data[2]        
            item = Item(date, shift, action)
            return item
        except ValueError:
            print("Invalid input! Please try again.")
    
    # this is how the item is represented in string    
    def __str__(self):
        return f"{self.date} -  {self.shift} - {self.action}"