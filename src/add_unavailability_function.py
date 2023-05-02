import csv
import datetime
from datetime import timedelta

# Main function to add unavailability 
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

    # Thursday of the following week

    #release_date_following_week + timedelta(days = 7))

    d=int(1)
    m=int(6)
    y=int(2023)
        
    release_date = datetime.datetime(y, m, d) 

    # Monday to Sunday of the week after the following week
    # Monday
    mon = (release_date + timedelta(days = 4)).strftime("%A %B %d %-Y")
    print("[1]", mon) 

    # Tuesday
    tue = (release_date + timedelta(days = 5)).strftime("%A %B %d %-Y")
    print("[2]", tue) 

    # Wednesday
    wed = (release_date + timedelta(days = 6)).strftime("%A %B %d %-Y")
    print("[3]", wed) 

    # Thursday
    thu = (release_date + timedelta(days = 7)).strftime("%A %B %d %-Y")
    print("[4]", thu) 

    # Friday
    fri = (release_date + timedelta(days = 8)).strftime("%A %B %d %-Y")
    print("[5]", fri) 

    # Saturday
    sat = (release_date + timedelta(days = 9)).strftime("%A %B %d %-Y")
    print("[6]", sat) 

    # Sunday
    sun = (release_date + timedelta(days = 10)).strftime("%A %B %d %-Y")
    print("[7]", sun)

    # Finish adding unavailability
    print("[Q] Enter Q to finish your selection\n")


    unavailable_days_dict = {
        "1": mon,
        "2": tue,
        "3": wed,
        "4": thu,
        "5": fri,
        "6": sat,
        "7": sun,
    }    

    unavailable_day = str()
    unavailable_day_selection = True
    selected_unavailable_days = []

    # Get users' input for unavailable days
    while unavailable_day_selection:
        unavailable_day = input("Please select your unavailable days: ")

        if (unavailable_day == "Q"):
            print("\n")
            print("THANK YOU! You have finished adding your unvailability.")
            print("\n")
            break
        
        elif unavailable_day in unavailable_days_dict:
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
                
                # Once all shift inputs are stored in a list, when users hit "Q" to quit the list is changed to a set to remove duplication if any
                elif unavailable_shift == "Q":
                    unavailable_shift_set = set(unavailable_shift_list)
                    print("--> You have finished seleting your unavailable shifts.")
                    break
                else:
                    print("--> Invalid input! Please try again.")

        
                # If users select an unavailable day but no shift is selected. The chosen day will not be marked as unavailable. 
                if len(unavailable_shift_set) == 0:
                    print(f'--> You are NOT marked as unavailable on {unavailable_days_dict[unavailable_day]}')
                
                # If all conditions are met, start appending users' input
                else:
                    with open(ua_file_name, "a") as ua_record:
                        unavailable_shift_string = ' '.join(unavailable_shift_set)  
                        writer = csv.writer(ua_record)
                        writer.writerow([unavailable_days_dict[unavailable_day], unavailable_shift_string, " Added"]) 
                        print(f'--> You have been marked as unavailable on {unavailable_days_dict[unavailable_day]} - {unavailable_shift_string}')
                        print("-" * 130)
                        print("\n")
                    ua_record.close()

        # Return warning for invalid input if users' selection for unavailable days are not listed in Prompt 2 or not equal to "Q"
        else:
            print("--> Invalid input! Please try again.")
