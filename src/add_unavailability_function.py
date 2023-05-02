import csv
import datetime
from datetime import timedelta
from create_roster_function import list_of_days, days_dict

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

    print(f'+{16*"-"}+')
    print("| UNAVAILABILITY |")
    print(f'+{16*"-"}+')


    # Start adding unavailability
    print("Enter index in the [] to select or enter Q to finish.")

    # Print out prompts as a list of day
    # Parameter is 14 because it is to generate the week after the following week
    list_of_days(14)

    unavailable_day = str()
    unavailable_day_selection = True
    selected_unavailable_days = []

    while unavailable_day_selection:
        unavailable_day = input("Please select your unavailable days: ")

        if (unavailable_day == "Q"):
            print("\n")
            print("THANK YOU! You have finished adding your unvailability.")
            print("\n")
            break
        
        elif unavailable_day in days_dict(14):
            # this method is to prompt user to select another day if the day they choose is already chosen previously
            if unavailable_day in selected_unavailable_days:
                print("--> Sorry you have selected this day! Please try again.")
                continue
            else:             
                selected_unavailable_days.append(unavailable_day)
            
            print("Enter AM, PM or Night to select or enter Q to finish.")
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
                    print("--> You have finished seleting your unavailable shifts.")
                    break
                else:
                    print("--> Invalid input! Please try again.")

        
            # If users select an unavailable day but no shift is selected. The chosen day will not be marked as unavailable. 
            with open(ua_file_name, "a") as ua_record:
                if len(unavailable_shift_set) == 0:
                    print(f'--> You are NOT marked as unavailable on {days_dict(14)[unavailable_day]}')
                
                # If all conditions are met, start appending users' input in the csv file
                else:
                    unavailable_shift_string = ' '.join(unavailable_shift_set)  
                    writer = csv.writer(ua_record)
                    writer.writerow([days_dict(14)[unavailable_day], unavailable_shift_string, " Added"]) 
                    print(f'--> You have been marked as unavailable on {days_dict(14)[unavailable_day]} - {unavailable_shift_string}')
                    print("\n")
                ua_record.close()

        # Return warning for invalid input if users' selection for unavailable days are not listed in Prompt 2 or not equal to "Q"
        else:
            print("--> Invalid input! Please try again.")
