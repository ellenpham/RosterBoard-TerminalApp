import csv 

def modify_roster():
    print("You are about to modify your work schedule....")

    #view the schedule again
    # open file in read mode --> reader = csv.reader(schedule_record)
    # row in reader
    # if rosters_day == row[0]
    #       list.append([rosters_day], "Modified")
    # else: list.append(row)

    # What would you like to modify?
    # Roster or Unavailability?
    # If roster:
    # What day would you like to modify?
    # List of their chosen day
    # Would you like to remove the day or change the shift?
    # Change shifts ---> Shift change ---> Modified


    with open("schedule_record.csv", 'r') as file:
        csvreader = csv.reader(file)
        print (csvreader)
        for row in csvreader:
            for r in row:
                print(r)
        
