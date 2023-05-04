import csv
import datetime 
from view_roster_function import view_schedule
from add_unavailability_function import add_unavailability
from create_roster_function import get_days_dict, display_weekday
from Roster import Roster
from Item import Item
from common_functions import *

file_name ="schedule_record.csv"
ua_file_name = "ua_record.csv"

# Main function to modify both availability and unavailability 
def modify_schedule():
    print("-" * 130)
    print("You are about to modify your work schedule....")
    
    # Function to modify roster(availability)
    def modify_roster():
        modify_option = str()

        # Keep looping users to select until they hit Q
        while modify_option != "Q":
            print ("\nDo you wish to modify or remove your chosen availability or add new availability?")
            print ("[1] Enter 1 to Modify")
            print ("[2] Enter 2 to Remove")
            print ("[3] Enter 3 to Add")
            print ("[Q] Enter Q to finish modifying your roster")
            modify_option = input("Enter your selection: ")
            print("\n")

            # Option 1: To modify a current availability
            if modify_option == "1":
                modify(file_name)
            
            # Option 2: To remove a current availability
            elif modify_option == "2":
                remove(file_name)

            # Option 3: To add a new availability
            elif modify_option == "3":
                add(file_name)
            
            # Enter Q to finish modification
            elif modify_option == "Q":
                # Checking again if rostered days are more than 3 after modification
                reader = csv.reader(open("schedule_record.csv"))
                line_count = len(list(reader))
                if line_count >= 4:
                    pass
                
                # If less than 3 days, notfy users of criteria for creating roster
                else: 
                    print(stylize("--> You are required to be available for at least THREE days. Do you want to CONTINUE to select more days?", warning_color()))

                    # Keep looping until users enter invalid answer
                    while True:
                        continue_or_not = input(stylize(f"--> Enter 'Yes' to continue or 'No' to quit: ", warning_color()))

                        # If no, clear all previously saved date in csv file  --> no roster recorded
                        if continue_or_not == "No":
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

                        # If yes, users are prompted back to continue add more days
                        elif continue_or_not == "Yes":
                            print("\n")
                            print(stylize("You have option to continue adding your available days. Please follow the prompts.", notice_color()))
                            break
                        else:
                            invalid_input_message()

            # Invalid input if users' selection is not listed or is not "Q"
            else:
                invalid_input_message()

    # Function to change a current rostered day's shift
    def modify(file_name):
        modified_rostered_day = str()
        
        # Initialize roster object
        users_roster = Roster()
        users_roster.load_from_file(file_name)
        users_roster.display_roster()

        # Create a dictionary for storing day item and its index
        currentitem_dict = dict()
        i = 1
        for item in users_roster.roster:
            currentitem_dict[str(i)] = item
            i += 1

        # Keep looping users to select until they hit Q
        while modified_rostered_day != "Q":
            print("Select the corresponding number in [] to choose the day you want to modify or enter Q to finish: ")
            modified_rostered_day = input("Enter your selection: ")
            
            # Break the loop if users hit Q
            if modified_rostered_day == "Q":
                break
            
            # If not Q, checking if the index selection is in dictionary's keys
            else:
                while True: 
                    # If yes, users can start change the current shift
                    if modified_rostered_day in currentitem_dict.keys():
                        modified_shift = input("Enter the shift you want to change to (AM, PM or Night): ")
                        # If shift input is valid, form a new day item then save new record to csv file
                        if check_valid_shift(modified_shift):
                            currentitem_dict[modified_rostered_day].shift = modified_shift
                            currentitem_dict[modified_rostered_day].action = "Modified"
                            users_roster.save_to_csv(file_name)
                            # Convert the date format to display a notice 
                            str_day = currentitem_dict[modified_rostered_day].day.strftime("%a %d/%m/%Y")
                            print(stylize(f'--> Your shift on {str_day} has been changed to {modified_shift}.', notice_color()))
                            break
                        # Invalid shift input
                        else:
                            invalid_input_message()

                    # If no, notify users that their day selection is not listed
                    else:
                        selection_not_in_list()
                        break

        
    # Function to remove a current rostered day
    def remove(file_name):
        removed_day = str()

        # Initialize roster object
        users_roster = Roster()
        users_roster.load_from_file(file_name)
        users_roster.display_roster()

        # Create a dictionary for storing day item and its index
        currentitem_dict = dict()
        i = 1
        for item in users_roster.roster:
            currentitem_dict[str(i)] = item
            i += 1

        # Keep looping users to select until they hit Q
        while removed_day != "Q":
            print("Select the corresponding number in [] to choose the day you want to remove or enter Q to finish: ")
            removed_day = input("Enter your selection: ")

            # Break the loop if users hit Q
            if removed_day == "Q":
                break
            
            # If not Q, checking if the index selection is in dictionary's keys
            else:
                # If yes, remove the chosen day from the roster list and save new record to csv file 
                if removed_day in currentitem_dict.keys():
                    users_roster.roster.remove(currentitem_dict[removed_day])
                    users_roster.save_to_csv(file_name)
                    # Convert the date format to display a notice 
                    str_day = currentitem_dict[removed_day].day.strftime("%a %d/%m/%Y")
                    print(stylize(f'--> Your shift on {str_day} has been removed.', notice_color()))

                # If no, notify users that their day selection is not listed
                else:
                    selection_not_in_list()
                

    # Function to add a new available day
    def add(file_name):
        added_day = str()
        
        # Initialize roster object
        users_roster = Roster()
        users_roster.load_from_file(file_name)

        # Display a list of days for users selection
        print("Please select a day in the below list: ")
        days_dict = get_days_dict(1)
        display_weekday(days_dict)

        # Keep looping users to select until they hit Q
        while added_day != "Q":
            print("Select the corresponding number in [] to choose the day you want to add or enter Q to finish: ")
            added_day = input("Enter your selection: ")
            
            # Break the loop if users hit Q
            if added_day == "Q":
                break
            
            # Notify users if their selection is not listed
            elif added_day not in days_dict:
                selection_not_in_list()
                pass
            
            # Define a variable to check if users seletct an existed day  
            else:
                existed_day = False

                # If yes, notify users that the day is already existed
                for item in users_roster.roster:
                    if item.day == days_dict[added_day]:
                        print(stylize("--> Sorry this day has been chosen! Please choose another day.", warning_color()))
                        existed_day = True
                        break

                # If no, start looping users for shift selection
                while not existed_day:
                    added_shift = input("Enter the shift you want to add (AM, PM or Night): ")

                    # If shift input is valid, form a new day item then save new record to csv file
                    if check_valid_shift(added_shift):
                        new_item = Item(days_dict[added_day], added_shift, action= "Modified")
                        users_roster.roster.append(new_item)
                        users_roster.save_to_csv(file_name)
                        # Convert the date format to display a notice 
                        str_day = new_item.day.strftime("%a %d/%m/%Y")
                        print(stylize(f'--> {str_day} - {added_shift} is added to your roster.', notice_color()))
                        break

                    # Invalid shift input
                    else:
                        invalid_input_message()


    # Function for modifying current unvailabiliy record
    def modify_unavailabilty():
        print("\n")
        print("If you choose to modify your unavailability, your old record will be cleared.")
        print("You will have to redo your unavailability from the scratch.")
        print("Do you wish to continue to modify your unavailability?")

        # Keep looping users for invalid answer
        # Prompt users to keep the current record or create new one
        while True:
            redo_or_not = input("Enter 'Yes' to redo or 'No' to keep your old record: ")
            
            # If no, make no change and display the current schedule
            if redo_or_not == "No":
                print('\n')
                print(stylize("There is no change made to your unavailability record.", notice_color()))
                print("-" * 130)
                view_schedule()
                break

            # If yes, clear the current data in csv file
            elif redo_or_not == "Yes":

                # Clear data in the csv file so users can rewrite from the scratch
                with open('ua_record.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows([" "])
                    f.close()
                with open('ua_record.csv', 'w') as f:
                    f.write("Unavailable days, Shifts, Action\n")
                    f.close()

                # Then prompt users to create new unavailability record
                add_unavailability(ua_file_name)
                break
            
            # Invalid input if users' input is not Yes or No
            else:
                invalid_input_message()


    modify_selection = str()

    # Prompt users to choose their option of what to modify
    # This is placed in the bottom because the imported functions are defined above
    # Keep looping users to select until they hit Q
    while modify_selection != "Q":
        print("\n")
        print("Please select your modification option: ")
        print("[1] Enter 1 to modify your current roster")
        print("[2] Enter 2 to modify your current unavailability record")
        print("[Q] Enter Q to back to Home Menu")
        modify_selection = input("Enter your selection: ")

        # Prompt 1 - Modify current roster
        if modify_selection == "1":
            modify_roster()

        # Prompt 3 - Modfy current unavailability record
        elif modify_selection == "2":
            modify_unavailabilty()
        
        # Hit Q to back to Home Menu
        elif modify_selection == "Q":
            print("\n")
            print(stylize("You have completed the modification!", notice_color()))
            print(stylize("Please Enter 3 in the Home Menu to review and confirm your up-to-date work schedule.", notice_color()))
            print("\n")
            break

        # Invalid input if users' selection is not listed or is not "Q"
        else:
            invalid_input_message()





        

        



