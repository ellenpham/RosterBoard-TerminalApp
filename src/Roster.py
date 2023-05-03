import csv 
from Item import Item
from common_functions import *

file_name = "schedule_record.csv"

# Define Roster class that represents the roster
class Roster:
    def __init__(self):
        self.roster = []
    
    # Load data from file to a list for temporary memory
    def load_from_file(self, file_name): 
        try:
            with open(file_name,"r") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
                for i in range(1, len(data)):
                    item = Item.from_str(data[i])
                    self.roster.append(item)
        except FileNotFoundError:
            print(stylize("Error found! There is no file to be read.", warning_color()))
        except Exception:
            print(stylize("It seems like something went wrong!", warning_color()))
    
    # Write to csv file
    def save_to_csv(self, file_name):
        try:
            with open(file_name, "w") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Rostered Day", "Shift", "Action"])
                for item in self.roster:
                    full_date = item.day.strftime("%a %d/%m/%Y")
                    csv_writer.writerow([full_date, item.shift, item.action])
        except Exception:
            print(stylize("Something happens! Data can not be saved to file.", warning_color()))
    
    # Display data from roster
    def display_roster(self):
        if not self.roster:
            print(stylize("Error found! The roster is empty.", warning_color()))
        else:
            print("Here is your current roster:")            
            print("Rostered days\t\tShift\tAction")
            i = 1
            for item in self.roster:
                day_str = item.day.strftime("%a %d/%m/%Y")
                print(f"[{i}] {day_str}\t{item.shift}\t{item.action}")
                i += 1

    
                

    




