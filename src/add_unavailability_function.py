import os
from create_roster_function import get_days_dict, display_weekday
from Unavailability import Unavailability
from Item import Item
from common_functions import *

def add_unavailability(ua_file_name):
    print("-" * 130)
    print("You are about to inform us of your unavailability for the week after the following week...")
    print("\n")
    print("**Important note**")
    print("\n")
    print("You can enter as many days and shifts as possible")
    print("By promptly notifying us if you have any planned leave, we can prepare a better workfore plan for our site.")
    print("-" * 130)
    print("Hit enter to start...")
    input()
    os.system('clear')

    print(f'+{16*"-"}+')
    print("| UNAVAILABILITY |")
    print(f'+{16*"-"}+')


    # Start adding unavailability
    print("Enter index in the [] to select or enter Q to finish.")

    # Print out prompts as a list of day
    days_dict = get_days_dict(2)
    display_weekday(days_dict)

    unavailable_day = str()
    unavailable_day_selection = True
    selected_unavailable_days = []
    ua_file_name = "ua_record.csv"

    # Initialize unavailabiity object
    users_unavailability = Unavailability()

    while unavailable_day_selection:
        unavailable_day = input("Please select your unavailable days: ")

        if (unavailable_day == "Q"):
            print("-" * 130)
            print("\n")
            print("THANK YOU! You have finished adding your unvailability.")
            print("\n")
            print("-" * 130)
            break
        
        elif unavailable_day in days_dict:
            # this method is to prompt user to select another day if the day they choose is already chosen previously
            if unavailable_day in selected_unavailable_days:
                print(stylize("--> Sorry you have selected this day! Please try again.", warning_color()))
                continue
            else:             
                selected_unavailable_days.append(unavailable_day)
            
            print("You can select multiple shifts. If you are unavailable all day, please select AM, PM and Night.")
            print("Enter AM, PM and Night to select or enter Q to finish:")
            print("[AM]    Enter AM for AM")
            print("[PM]    Enter PM for PM")
            print("[Night] Enter Night for Night")
            print("[Q]     Enter Q to finish your selection")
            
            unavailable_shift = str()
            unavailable_shift_list = []
            unavailable_shift_set = {}

            while unavailable_shift != "Q":
                unavailable_shift = input("Please select your unavailable shifts: ")

                # only valid shift inputs (AM, PM, Night) are added in the list
                if unavailable_shift == "AM":
                    unavailable_shift_list.append(unavailable_shift)
                    pass

                elif unavailable_shift == "PM":
                    unavailable_shift_list.append(unavailable_shift)
                    pass
                
                elif unavailable_shift == "Night":
                    unavailable_shift_list.append(unavailable_shift)
                    pass
                
                # Once all shift inputs are stored in a list, the list is changed to a set to remove duplication if any
                elif unavailable_shift == "Q":
                    unavailable_shift_set = set(unavailable_shift_list)
                    print(stylize("--> You have finished selecting your unavailable shifts.", notice_color()))
                    break
                else:
                    invalid_input_message()

            
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
                

        # Return warning for invalid input if users' selection for unavailable days are not listed in Prompt 2 or not equal to "Q"
        else:
            invalid_input_message()
