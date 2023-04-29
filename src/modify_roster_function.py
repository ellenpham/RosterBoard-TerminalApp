import csv
from view_roster_function import view_schedule


def modify_schedule():
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("You are about to modify your work schedule....")
    file_name ="schedule_record.csv"
    def modify_roster():
        modify_option = str()

        while modify_option != "Q":
            print ("\nDo you wish to modify, remove your chosen availability or add a new availability?")
            print ("[1] Enter 1 to Modify")
            print ("[2] Enter 2 to Remove")
            print ("[3] Enter 3 to Add")
            print ("[Q] Enter Q to Quit")
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
    modify_roster()

    # ---> there is problem with remove(file_name) is called out before assignment --> need to fix

    # To modify chosen rostered day
    # still have problem where if user already removed a day, then they go back to modify and if it's less than 2 days --> still print their roster. 
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

    modify(file_name)
                    
    def checking_roster():
        reader = csv.reader(open("schedule_record.csv"))
        line_count = len(list(reader))
        if line_count >= 4:
            pass

        else: # if less than 3 available days, users can choose to continue adding more days or have no roster at all
            print("--> You are required to be available for at least THREE days. Do you want to CONTINUE to select more days?")
            # Error handling for users input for continue-or-not prompt
            while True:
                continue_or_not = input ("--> Enter 'Yes' to continue or 'No' to quit: ")
                if continue_or_not == "No":
                    print("---------------------------------------------------------------------------------")
                    print("You have no roster for the following week.")
                    print("Please review and confirm your up-to-date work schedule")
                    print("-------------------------------------------------------------------------------- ")
                    view_schedule()
                    break
                elif continue_or_not == "Yes":
                    print("\n")
                    print("You have option to continue adding your available days. Please follow the prompts.")
                    print("\n")
                    break
                else:
                    print("Invalid input! Please try again.")
    checking_roster()
        
    # To remove chosen rostered day
    def remove(file_name):
        removed_day = str()
        while True:
            removed_day = input("Enter the day you want to remove or enter Q to finish: ")

            if removed_day == "Q":
                break
            else:
                removed_days_list = []
                with open(file_name, "r") as schedule_record:
                    csv_reader = csv.reader(schedule_record)
                    for row in csv_reader:
                        removed_days_list.append(row)
                        for day in row:
                            if day == removed_day:
                                removed_days_list.remove(row)
                    print(removed_days_list)
                with open(file_name, "w") as schedule_record:
                    writer = csv.writer(schedule_record)
                    writer.writerows(removed_days_list)
                    print(f'--> {removed_day} has been removed from your roster.')
    remove(file_name)

    # Re-checking if the number of rostered days is less than 3  ---> TRY TO MODIFY CODE IN PROMPT 1 TO MAKE THIS A FUNCTION TO CALL
    checking_roster()

    # To add more days to roster
    def add(file_name):
        added_day_list =[]
        added_day = str()
        while True:
            added_day = input("Enter the day you want to add or enter Q to finish: ")

            if added_day == "Q":
                break

            else:
                with open(file_name, "a") as schedule_record:
                    added_day_list.append(added_day)
                    writer = csv.writer(schedule_record)
                    writer.writerow([added_day, " Modified"])
                print(f'--> {added_day} is added to your roster.')

        # 3 more issues needed to cover
        # display the list of day again
        # add shift
        # can not add if it's duplicated
        # if it's still less than 3 days --> add more
        # ---> TRY TO MODIFY CODE IN PROMPT 1 TO MAKE THIS A FUNCTION TO CALL


    # To update unavailability
    def modify_unavailabilty(ua_file_name):
        pass
    
   
    # Prompt users to choose their option of what to modify
    modify_selection = str()
    file_name = "schedule_record.csv"
    ua_file_name = "ua_record.csv"

    while modify_selection != "Q":
        print("\n")
        print("Please select your modification option: ")
        print("[1] Enter 1 to modify your roster for the following week")
        print("[2] Enter 2 to modify your recorded unavailability for the week after the following week")
        print("[Q] Enter Q to back to Home Menu")
        modify_selection = input("Enter your selection: ")

        if modify_selection == "1":
            modify_roster(file_name)

        elif modify_selection == "2":
            modify_unavailabilty(ua_file_name)
        
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



        

        



