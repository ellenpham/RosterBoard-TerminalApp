import csv 
from Item import Item

file_name = "schedule_record.csv"

# define the Roster class that represent the roster
class Roster:
    def __init__(self):
        self.roster = []
    
    # Load data from file to a list
    def load_from_file(self, file_name): 
        try:
            with open(file_name,"r") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
                for i in range(1, len(data)):
                    item = Item.from_str(data[i])
                    self.roster.append(item)
        except FileNotFoundError:
            print("Error reading file.")
        except Exception:
            print("Something went wrong!")
    
    # Write to csv file
    def save_to_csv(self, file_name):
        try:
            with open(file_name, "w") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Rostered Day", "Shift", "Action"])
                for item in self.roster:
                    full_date = item.date.strftime("%a %d/%m/%Y")
                    csv_writer.writerow([full_date, item.shift, item.action])
        except Exception:
            print("Can not save to file.")
    
    # Display data from roster
    def display_roster(self):
        if not self.roster:
            print("The roster is empty")
        else:            
            print("Rostered days\t\tShift\tAction")
            i = 1
            for item in self.roster:
                date_str = item.date.strftime("%a %d/%m/%Y")
                print(f"[{i}] {date_str}\t{item.shift}\t{item.action}")
                i += 1

    
                

    




