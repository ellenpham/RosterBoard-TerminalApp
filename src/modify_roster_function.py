import csv
import datetime 
from view_roster_function import view_schedule
from add_unavailability_function import add_unavailability
from create_roster_function import check_valid_shift

# Function to check if users input is in correct date format
def is_date(string, fmt="%A %B %d %Y"):
    try:
        datetime.datetime.strptime(string, fmt)
        return True
    except ValueError:
        return False

# Function to check if a day is already existed in the record ---> NEED TO FIX
def check_existed_day(day):
    file_name = "schedule_record.csv"
    selected_day = []
    with open(file_name, "r") as schedule_record:
        reader = csv.reader(schedule_record)
        selected_day == list(reader)

        if day in selected_day:
            return True
        else:             
            return False

# Main function to modify both availability and unavailability 
def modify_schedule():
    file_name ="schedule_record.csv"
    ua_file_name = "ua_record.csv"

    print("-" * 130)
    print("You are about to modify your work schedule....")
    
    # Function to modify roster(availability)
    def modify_roster():
        modify_option = str()

        while modify_option != "Q":
            print ("\nDo you wish to modify, remove your chosen availability or add a new availability?")
            print ("[1] Enter 1 to Modify")
            print ("[2] Enter 2 to Remove")
            print ("[3] Enter 3 to Add")
            print ("[Q] Enter Q to finish modifying your roster")
            modify_option = input("Enter your selection: ")
            print("\n")

            if modify_option == "1":
                modify(file_name)
            
            elif modify_option == "2":
                remove(file_name)

            elif modify_option == "3":
                add(file_name)

            elif modify_option == "Q":
                # Checking again if rostered days are more than 3 days after modification
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
                            # clear all records in the roster due to less than 3 available days
                            with open('schedule_record.csv', 'w') as f:
                                writer = csv.writer(f)
                                writer.writerows([" "])
                                f.close()
                            with open('schedule_record.csv', 'w') as f:
                                f.write("Rostered days, Shift, Action\n")
                                f.close()
                            print("-" * 110)
                            print("You have no roster for the following week.")
                            print("Please review and confirm your up-to-date work schedule")
                            print("-" * 110)
                            view_schedule()
                            break
                        elif continue_or_not == "Yes":
                            print("\n")
                            print("You have option to continue adding your available days. Please follow the prompts.")
                            break
                        else:
                            print("Invalid input! Please try again.")

            # Return warning for invalid input if users' selection are not listed in the prompt to Modfy, Remove or Add or not equal to "Q"
            else:
                print("Invalid input! Please try again.")

    # To modify chosen rostered day
    def modify(file_name):
        modified_rostered_day =str()

        while modified_rostered_day != "Q":
            print("Please follow this example format to enter day: 'Monday May 01 2023'")
            modified_rostered_day = input("Enter the day you want to modify or enter Q to finish: ")
            
            if modified_rostered_day == "Q":
                break
            
            # check if users' input is in give date format
            elif not is_date(modified_rostered_day):
                print ("Invalid input! Please try again")

            else:
                while True: 
                    modified_shift = input("Enter the shift you want to change to (AM, PM or Night): ")
                    if not check_valid_shift(modified_shift):
                        pass
                    # if all conditions are met, start reading the csv file then overriding the old records
                    else:
                        rostered_days_list = []
                        with open(file_name, "r") as schedule_record:
                            csv_reader = csv.reader(schedule_record)
                            for row in csv_reader:
                                if modified_rostered_day == row[0]:
                                    rostered_days_list.append([modified_rostered_day, modified_shift, "Modified"])
                                else:
                                    rostered_days_list.append(row)
                        schedule_record.close()
                        print(rostered_days_list)  #---> Remove when complete
            
                        with open(file_name, "w") as schedule_record:
                            writer = csv.writer(schedule_record)
                            writer.writerows(rostered_days_list)
                            schedule_record.close()
                        print(f'--> Your shift on {modified_rostered_day} has been changed to {modified_shift}.\n')
                        break

        # ---> still print if users choose a day this not in roster --> NEED TO FIX
        
    # To remove chosen rostered day
    def remove(file_name):
        removed_day = str()
        while removed_day != "Q":
            print("Please follow this example format to enter day: 'Monday May 01 2023'")
            removed_day = input("Enter the day you want to remove or enter Q to finish: ")

            if removed_day == "Q":
                break

            # check if users' input is in give date format
            elif not is_date(removed_day):
                print ("Invalid input! Please try again")
            
            # if all conditions are met, start reading the csv file then removing the old records
            else:
                removed_days_list = []
                with open(file_name, "r") as schedule_record:
                    csv_reader = csv.reader(schedule_record)
                    for row in csv_reader:
                        removed_days_list.append(row)
                        for day in row:
                            if day == removed_day:
                                removed_days_list.remove(row)
                    schedule_record.close()
                print(removed_days_list) # --> delete when complete
                with open(file_name, "w") as schedule_record:
                    writer = csv.writer(schedule_record)
                    writer.writerows(removed_days_list)
                    schedule_record.close()
                print(f'--> {removed_day} has been removed from your roster.\n')
                    
    # ---> still print if users choose a day this not in roster --> NEED TO FIX

    # To add more days to roster
    def add(file_name):
        added_day_list =[]
        added_day = str()
           
        while added_day != "Q":
            print("Please follow this example format to enter day: 'Monday May 01 2023'")
            added_day = input("Enter the day you want to add or enter Q to finish: ")
            
            if added_day == "Q":
                break
            
            # check if users' input is in give date format
            elif not is_date(added_day):
                print ("Invalid input! Please try again")
        
            else:
                # ---> still can not detect duplicated days --> NEED TO FIX
                # check if users' chosen day is already existed in the csv file --> then they need to choose another day to add
                if check_existed_day(added_day):
                    print("--> Sorry you have selected this day! You can only select ONE shift per day.")
                    modify_roster()

                else:
                    while True: 
                        added_shift = input("Enter the shift you want to add (AM, PM or Night): ")
                        if not check_valid_shift(added_shift):
                            pass

                        # if all conditions are met, start reading the csv file then adding the new records
                        else:            
                            with open(file_name, "a") as schedule_record:
                                added_day_list.append(added_day)
                                writer = csv.writer(schedule_record)
                                writer.writerow([added_day, added_shift, " Modified"])
                                print(f'--> {added_day} - {added_shift} is added to your roster.\n')
                                schedule_record.close()
                            break


    # To modify unavailability record
    def modify_unavailabilty():
        print("\n")
        print("If you choose to modify your unavailability, your old record will be cleared.")
        print("You will have to redo your unavailability from the sratch.")
        print("Do you wish to continue to modify your unavailability?")
        while True:
            redo_or_not = input("Enter 'Yes' to redo or 'No' to keep your old record: ")
            
            if redo_or_not == "No":
                print('\n')
                print("There is no change made to your unavailability record.")
                view_schedule()

            elif redo_or_not == "Yes":

                # can create a function?? ---> NEED TO FIX
                # clear data in the csv file so users can rewrite from the scratch
                with open('ua_record.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows([" "])
                    f.close()
                with open('ua_record.csv', 'w') as f:
                    f.write("Unavailable days, Shifts, Action\n")
                    f.close()

                add_unavailability(ua_file_name)
                break
            
            else:
                print("Invalid input! Please try again.")

    # Prompt users to choose their option of what to modify
    # This is placed in the bottom because the imported functions are defined above
    modify_selection = str()

    while modify_selection != "Q":
        print("\n")
        print("Please select your modification option: ")
        print("[1] Enter 1 to modify your roster for the following week")
        print("[2] Enter 2 to modify your recorded unavailability for the week after the following week")
        print("[Q] Enter Q to back to Home Menu")
        modify_selection = input("Enter your selection: ")

        if modify_selection == "1":
            modify_roster()

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





        

        



