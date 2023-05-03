import csv 
from Item import Item
from common_functions import *

file_name = "ua_record.csv"

# define the Unavailability class that represents unavailability record
class Unavailability:
    def __init__(self):
        self.unavailability = []
    
    # Load data from file to a list for temporary memory
    def load_from_file(self, file_name): 
        try:
            with open(file_name,"r") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
                for i in range(1, len(data)):
                    item = Item.from_str(data[i])
                    self.unavailability .append(item)
        except FileNotFoundError:
            print(stylize("Error found! There is no file to be read.", warning_color()))
        except Exception:
            print(stylize("It seems like something went wrong!", warning_color()))
    
    # Write to csv file
    def save_to_csv(self, file_name):
        try:
            with open(file_name, "w") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Unavailable Days", "Shifts", "Action"])
                for item in self.unavailability:
                    full_date = item.day.strftime("%a %d/%m/%Y")
                    csv_writer.writerow([full_date, item.shift, item.action])
        except Exception:
            print(stylize("Something happens! Data can not be saved to file.", warning_color()))
    
    # Display data from unavailability record
    def display_unavailability (self):
        if not self.unavailability :
            print(stylize("Error found: There is no record in the file.", warning_color()))
        else:
            print("Here is your current unavailability record: ")              
            print("Unavailable days\t\tShifts\tAction")
            i = 1
            for item in self.unavailability :
                date_str = item.day.strftime("%a %B %d %Y")
                print(f"[{i}] {date_str}\t{item.shift}\t{item.action}")
                i += 1
