import os
from create_roster_function import get_days_dict, display_weekday
from Unavailability import Unavailability
from Item import Item
from common_functions import *

# Main function for adding unvailability
def add_unavailability(ua_file_name):
    print("-" * 130)
    print("You are about to inform us of your unavailability for the week after the following week...")
    print("\n")
    print("**Important note**")
    print("\n")
    print("You can enter as many days and shifts as possible")
    print("By promptly notifying us of your planned leave, we can prepare a better workfore plan for our site.")
    print("-" * 130)
    print("Hit enter to start...")
    input()
    os.system('clear')

    print(f'+{16*"-"}+')
    print("| UNAVAILABILITY |")
    print(f'+{16*"-"}+')


    # Start adding unavailability
    print("Enter index in the [] to select or enter Q to finish.")

    # Print out the list of day selection 
    days_dict = get_days_dict(2)
    display_weekday(days_dict)

    unavailable_day = str()
    unavailable_day_selection = True
    selected_unavailable_days = []
    ua_file_name = "ua_record.csv"

    # Initialize unavailabiity object
    users_unavailability = Unavailability()

    # Start looping users to select the days until they hit Q to quit
    while unavailable_day_selection:
        unavailable_day = input("Please select your unavailable day: ")

        # If they hit Q, the task is finished
        if (unavailable_day == "Q"):
            print("-" * 130)
            print("\n")
            print("THANK YOU! You have finished adding your unvailability.")
            print("\n")
            print("-" * 130)
            break
        
        # Else if the chosen days are in the days dictionary
        elif unavailable_day in days_dict:
            # Check if the day is already chosen to prevent duplication
            if unavailable_day in selected_unavailable_days:
                print(stylize("--> Sorry you have selected this day! Please try again.", warning_color()))
                continue
            else:             
                selected_unavailable_days.append(unavailable_day)
            
            # Shifts selection comes after a day is successfully chosen
            print("You can select multiple shifts. If you are unavailable all day, please select AM, PM and Night.")
            print("Enter AM, PM and Night to select or enter Q to finish:")
            print("[AM]    Enter AM for AM")
            print("[PM]    Enter PM for PM")
            print("[Night] Enter Night for Night")
            print("[Q]     Enter Q to finish your selection")
            
            # Start looping users to select shifts until they hit Q to quit
            unavailable_shift = str()
            unavailable_shift_list = []
            unavailable_shift_set = {}

            while unavailable_shift != "Q":
                unavailable_shift = input("Please select your unavailable shifts: ")

                # Only valid shift inputs (AM, PM, Night) are added in the list
                if unavailable_shift == "AM":
                    unavailable_shift_list.append(unavailable_shift)
                    pass

                elif unavailable_shift == "PM":
                    unavailable_shift_list.append(unavailable_shift)
                    pass
                
                elif unavailable_shift == "Night":
                    unavailable_shift_list.append(unavailable_shift)
                    pass
                
                # Once all shift inputs are stored in a list, the list is converted to a set to remove duplication if any
                elif unavailable_shift == "Q":
                    unavailable_shift_set = set(unavailable_shift_list)
                    print(stylize("--> You have finished selecting your unavailable shifts.", notice_color()))
                    break

                # If a shift input is not AM, PM, Night or Q, it is invalid
                else:
                    invalid_input_message()

            # The format of day is converted before displaying
            day_str = days_dict[unavailable_day].strftime("%a %d/%m/%Y")

            # If users select an unavailable day but no shift is selected. The chosen day will not be marked as unavailable. 
            if len(unavailable_shift_set) == 0:
                print(stylize(f'--> You are NOT marked as unavailable on {day_str}', notice_color()))
            
            # If all conditions are met, start appending users' input in the csv file
            else:
                unavailable_shift_string = ' '.join(unavailable_shift_set) 
                new_item = Item(days_dict[unavailable_day], unavailable_shift_string, action = "Added")
                users_unavailability.unavailability.append(new_item)
                users_unavailability.save_to_csv(ua_file_name)
                print(stylize(f'--> You have been marked as unavailable on {day_str} - {unavailable_shift_string}', notice_color()))
                

        # Invalid input if users' days selection is not listed or is not "Q"
        else:
            invalid_input_message()
