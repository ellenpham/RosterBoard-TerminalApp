import csv

def modify_schedule():
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("You are about to modify your work schedule....")

    def modify_roster(file_name):
        print ("Would you like to modify, remove your chosen availability or add a new availability?")
        print ("[1] Enter 1 to Modify")
        print ("[2] Enter 2 to Remove")
        print ("[3] Enter 3 to Add")
        print ("[Q] Enter Q to Quit")
        
        while modify_option != "Q":
            modify_option = input("Enter your selection: ")

            if modify_option == "1":
                modify(file_name)
            
            elif modify_option == "2":
                remove(file_name)

            elif modify_option == "3":
                add(file_name)

            elif modify_option == "Q":
                break

            else:
                print("Invalid input! Please try again.")  
        
        
        def modify(file_name):
            while True:
                modified_rostered_day = input("Enter the day you want to modify or enter Q to finish: ")

                if modified_rostered_day == "Q":
                    break

                else:
                    modified_shift = input("Enter the shift you want to change to: ")
                    rostered_days_list = []
                    with open(file_name, "r") as schedule_record:
                        csv_reader = csv.reader(schedule_record)
                        for row in csv_reader:
                            if modified_rostered_day == row[0]:
                                rostered_days_list.append([modified_rostered_day, modified_shift, "Modified"])
                            else:
                                rostered_days_list.append(row)
                    print(rostered_days_list)  #---> Remove when complete
                    
                    with open(file_name, "w") as schedule_record:
                        writer = csv.writer(schedule_record)
                        writer.writerows(rostered_days_list)
                        print(f'--> Your shift on {modified_rostered_day} has been changed to {modified_shift}.')
            

        def remove(file_name):
            pass

        def add(file_name):
            pass
        


    def modify_unavailabilty():
        pass
    
   

    # Prompt users to choose their option of what to modify
    modify_selection = str()
    file_name = "schedule_record.csv"

    while modify_selection != "Q":
        print("\n")
        print("Please select your option: ")
        print("[1] Enter 1 to modify your roster for the following week")
        print("[2] Enter 2 to modify your recored unavailability for the week after the following week")
        print("[Q] Enter Q to back to Home Menu")
        print("\n")
        modify_selection = input("Enter your selection: ")

        if modify_selection == "1":
            modify_roster(file_name)

        elif modify_selection == "2":
            modify_unavailabilty()
        
        elif modify_selection == "Q":
            print("\n")
            print("You have completed the modification!")
            print("Please Enter 3 in the Home Menu to review and confirm your up-to-date work schedule.")
            print("\n")
            break
        else:
            print("Invalid input! Please try again.")


        

        # What would you like to modify?
        # Roster or Unavailability?
        # If roster:
        # What day would you like to modify?
        # List of their chosen day
        # Would you like to remove the day or change the shift?
        # What day would you like to change?
        # Change shifts ---> Shift change ---> Modified
        # Remove day
        # What day would you like to remove?
        # Do you want to add more days?



        

        



