import csv
import datetime 
from view_roster_function import view_schedule
from add_unavailability_function import add_unavailability
from create_roster_function import get_days_dict, display_weekday
from Roster import Roster
from Item import Item
from common_functions import *

# Function to check if users input is in correct date format
def is_date(string, fmt="%A %B %d %Y"):
    try:
        datetime.datetime.strptime(string, fmt)
        return True
    except ValueError:
        return False

file_name ="schedule_record.csv"
ua_file_name = "ua_record.csv"



# Main function to modify both availability and unavailability 
def modify_schedule():
    print("-" * 130)
    print("You are about to modify your work schedule....")
    
    # Function to modify roster(availability)
    def modify_roster():
        modify_option = str()

        while modify_option != "Q":
            print ("\nDo you wish to modify or remove your chosen availability or add new availability?")
            print ("[1] Enter 1 to Modify")
            print ("[2] Enter 2 to Remove")
            print ("[3] Enter 3 to Add")
            print ("[Q] Enter Q to finish modifying your roster")
            modify_option = input("Enter your selection: ")

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
                    print(stylize("--> You are required to be available for at least THREE days. Do you want to CONTINUE to select more days?", warning_color()))
                    # Error handling for users input for continue-or-not prompt
                    while True:
                        continue_or_not = input(stylize(f"--> Enter 'Yes' to continue or 'No' to quit: ", warning_color()))
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
                            print(stylize("You have option to continue adding your available days. Please follow the prompts.", notice_color()))
                            break
                        else:
                            invalid_input_message()

            # Return warning for invalid input if users' selection are not listed in the prompt to Modfy, Remove or Add or not equal to "Q"
            else:
                invalid_input_message()

    # To modify chosen rostered day
    def modify(file_name):
        modified_rostered_day = str()
        
        # Initialize roster object
        users_roster = Roster()
        users_roster.load_from_file(file_name)
        users_roster.display_roster()
        currentitem_dict = dict()
        i = 1
        for item in users_roster.roster:
            currentitem_dict[str(i)] = item
            i += 1

        while modified_rostered_day != "Q":
            modified_rostered_day = input("Enter the day you want to modify or enter Q to finish: ")
            
            if modified_rostered_day == "Q":
                break

            else:
                while True: 
                    if modified_rostered_day in currentitem_dict.keys():
                        modified_shift = input("Enter the shift you want to change to (AM, PM or Night): ")
                        if check_valid_shift(modified_shift):
                            currentitem_dict[modified_rostered_day].shift = modified_shift
                            currentitem_dict[modified_rostered_day].action = "Modified"
                            users_roster.save_to_csv(file_name)
                            str_day = currentitem_dict[modified_rostered_day].day.strftime("%a %d/%m/%Y")
                            print(stylize(f'--> Your shift on {str_day} has been changed to {modified_shift}.', notice_color()))
                            break
                        else:
                            invalid_input_message()
                    
                    else:
                        selection_not_in_list()
                        break

        
    # To remove chosen rostered day
    def remove(file_name):
        removed_day = str()

        # Initialize roster object
        users_roster = Roster()
        users_roster.load_from_file(file_name)
        users_roster.display_roster()
        currentitem_dict = dict()
        i = 1
        for item in users_roster.roster:
            currentitem_dict[str(i)] = item
            i += 1

        while removed_day != "Q":
            removed_day = input("Enter the day you want to remove or enter Q to finish: ")

            if removed_day == "Q":
                break
          
            else:
                if removed_day in currentitem_dict.keys():
                    users_roster.roster.remove(currentitem_dict[removed_day])
                    users_roster.save_to_csv(file_name)
                    str_day = currentitem_dict[removed_day].day.strftime("%a %d/%m/%Y")
                    print(stylize(f'--> Your shift on {str_day} has been removed.', notice_color()))
                else:
                    selection_not_in_list()
                

    # To add more days to roster
    def add(file_name):
        added_day = str()
        
        # Initialize roster object
        users_roster = Roster()
        users_roster.load_from_file(file_name)

        print("Please select a day in the below list: ")
        days_dict = get_days_dict(1)
        display_weekday(days_dict)
           
        while added_day != "Q":
            added_day = input("Enter the day you want to add or enter Q to finish: ")
            
            if added_day == "Q":
                break

            elif added_day not in days_dict:
                selection_not_in_list()
                pass

            else:
                existed_day = False

                for item in users_roster.roster:
                    if item.day == days_dict[added_day]:
                        print(stylize("--> Sorry this day has been chosen! Please choose another day.", warning_color()))
                        existed_day = True
                        break
                       
                while not existed_day:
                    added_shift = input("Enter the shift you want to add (AM, PM or Night): ")
                    if check_valid_shift(added_shift):
                        new_item = Item(days_dict[added_day], added_shift, action= "Added")
                        users_roster.roster.append(new_item)
                        users_roster.save_to_csv(file_name)
                        str_day = new_item.day.strftime("%a %d/%m/%Y")
                        print(stylize(f'--> {str_day} - {added_shift} is added to your roster.', notice_color()))
                        break
                    else:
                        invalid_input_message()


    # To modify unavailability record
    def modify_unavailabilty():
        print("\n")
        print("If you choose to modify your unavailability, your old record will be cleared.")
        print("You will have to redo your unavailability from the scratch.")
        print("Do you wish to continue to modify your unavailability?")
        while True:
            redo_or_not = input("Enter 'Yes' to redo or 'No' to keep your old record: ")
            
            if redo_or_not == "No":
                print('\n')
                print(stylize("There is no change made to your unavailability record.", notice_color()))
                print("-" * 130)
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
                invalid_input_message()

    # Prompt users to choose their option of what to modify
    # This is placed in the bottom because the imported functions are defined above
    modify_selection = str()

    while modify_selection != "Q":
        print("\n")
        print("Please select your modification option: ")
        print("[1] Enter 1 to modify your current roster")
        print("[2] Enter 2 to modify your current unavailability record")
        print("[Q] Enter Q to back to Home Menu")
        modify_selection = input("Enter your selection: ")

        if modify_selection == "1":
            modify_roster()

        elif modify_selection == "2":
            modify_unavailabilty()
        
        elif modify_selection == "Q":
            print("\n")
            print(stylize("You have completed the modification!", notice_color()))
            print(stylize("Please Enter 3 in the Home Menu to review and confirm your up-to-date work schedule.", notice_color()))
            print("\n")
            break
        else:
            invalid_input_message()





        

        



