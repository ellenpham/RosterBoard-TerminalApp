import datetime
from datetime import timedelta
import csv 

# Function to check if user put in correct shifts
def check_valid_shift(shift):
    if shift == "AM" or shift == "PM" or shift == "Night":
        return True
    else:
        print("Invalid input! Please try again.")
        return False

# Function using weekday() method and datetime.timedelta() to always get next week's Monday
# i is the parameter, if i = 7 then function will return results of next week 
# if i = 14 then function will return results of the week after next week 
def get_next_monday(i):
    today  = datetime.date.today()
    days_to_next_monday = i - today.weekday()
    next_monday = today + datetime.timedelta(days = days_to_next_monday)
    return next_monday

# Print out a list of available days for users selection
def list_of_days(i):
    mon = get_next_monday(i).strftime("%A %B %d %-Y")
    print("[1]", mon) 

    # get next Tuesday
    next_tue = get_next_monday(i) + datetime.timedelta(days = 1)
    tue = next_tue.strftime("%A %B %d %-Y")
    print("[2]", tue) 

    # get next Wednesday
    next_wed = get_next_monday(i) + datetime.timedelta(days = 2)
    wed = next_wed.strftime("%A %B %d %-Y")
    print("[3]", wed) 

    # get next Thursday
    next_thu = get_next_monday(i) + datetime.timedelta(days = 3)
    thu = next_thu.strftime("%A %B %d %-Y")
    print("[4]", thu) 

    # get next Friday
    next_fri = get_next_monday(i) + datetime.timedelta(days = 4)
    fri = next_fri.strftime("%A %B %d %-Y")
    print("[5]", fri) 

    # get next Saturday
    next_sat = get_next_monday(i) + datetime.timedelta(days = 5)
    sat = next_sat.strftime("%A %B %d %-Y")
    print("[6]", sat) 

    # get next Sunday
    next_sun = get_next_monday(i) + datetime.timedelta(days = 6)
    sun = next_sun.strftime("%A %B %d %-Y")
    print("[7]", sun)

    # Finish creating roster
    print("[Q] Enter Q to finish your selection\n")

# Put days in a dictionary
def days_dict(i):
    mon = get_next_monday(i).strftime("%A %B %d %-Y")

    next_tue = get_next_monday(i) + datetime.timedelta(days = 1)
    tue = next_tue.strftime("%A %B %d %-Y")

    next_wed = get_next_monday(i) + datetime.timedelta(days = 2)
    wed = next_wed.strftime("%A %B %d %-Y")

    next_thu = get_next_monday(i) + datetime.timedelta(days = 3)
    thu = next_thu.strftime("%A %B %d %-Y")

    next_fri = get_next_monday(i) + datetime.timedelta(days = 4)
    fri = next_fri.strftime("%A %B %d %-Y")

    next_sat = get_next_monday(i) + datetime.timedelta(days = 5)
    sat = next_sat.strftime("%A %B %d %-Y")

    next_sun = get_next_monday(i) + datetime.timedelta(days = 6)
    sun = next_sun.strftime("%A %B %d %-Y")

    dict = {
        "1": mon,
        "2": tue,
        "3": wed,
        "4": thu,
        "5": fri,
        "6": sat,
        "7": sun,
    }
    return dict

# Main function for creating roster
def create_roster(file_name):
    print("-" * 130)
    print("You are about to create your roster for the following week...")
    print("\n")
    print("**Important note**")
    print("\n")
    print("You are required to be available for at least THREE days.")
    print("If you select less than THREE days of work, you will have no roster for the following week.")
    print("If you select THREE days or more, you will get rostered for all of the available days that you have chosen.")
    print("You can only select ONE available shift, shift duration is 5 hours, anything over will get counted to your overtime rate.")
    print("-" * 130)
    print("Hit enter to start...")
    input()

    print(f'+{14*"-"}+')
    print("| AVAILABILITY |")
    print(f'+{14*"-"}+')

    # Start creating roster
    print("Enter index in the [] to select or enter Q to finish.")

    list_of_days(7)
    
    # Get users' input for available days
    available_day = str()
    user_day_selection = True
    selected_day = []
    file_name = "schedule_record.csv"

    while user_day_selection:
        available_day = input("Please select your available days: ")

        '''
        user_day_selection = False (it means users finish creating their roster) in the following cases:
        1. Three or more days (no duplication) have been chosen before users hit 8 to quit 
            --> Successfully created roster --> Back to Home Menu
        2. users choose two available days but do not want to continue to add more days 
            --> No roster is created --> Back to Home Menu
        
        If users keep enter invalid input and none of the above cases is met.
        user_input_selection will keep looping until one of the above condition is met. 
        '''
        if (available_day == "Q"):
            # count data from csv file to check how many available days are already recorded
            # if more than 3 available days then users have completed creating roster
            csv_reader = csv.reader(open("schedule_record.csv"))
            line_count = len(list(csv_reader))
            if line_count >= 4:
                user_day_selection = False
                print("\nTHANK YOU! You have completed your roster for the following week.")
                print("You have the option to view your roster again in the Home Menu.\n")
                print("-" * 130)
                print("\n")
                break
        

            else: # if less than 3 available days, users can choose to continue adding more days or have no roster at all
                print("--> You are required to be available for at least THREE days. Do you want to CONTINUE to select more days?")
                # Error handling for users input for continue-or-not prompt
                while True:
                    continue_or_not = input ("--> Enter 'Yes' to continue or 'No' to quit: ")
                    if continue_or_not == "No":
                        user_day_selection = False
                        # clear all records in the roster because if less than 3 days, users do not get rostered
                        with open('schedule_record.csv', 'w') as f:
                            writer = csv.writer(f)
                            writer.writerows([" "])
                            f.close()

                        with open('schedule_record.csv', 'w') as f:
                            f.write("Rostered days, Shift, Action\n")
                            f.close()
                        print("-" * 110)
                        print("You have no roster for the following week.")
                        print("If you need further discussion, please contact our HR department on 1300 123 456.")
                        print("-" * 110)
                        break
                    elif continue_or_not == "Yes":
                        break
                    else:
                        print("Invalid input! Please try again.")

        elif available_day in days_dict(7):
            # Restrict users' selection of 2 same days. 
            if available_day in selected_day:
                print("--> Sorry you have selected this day! You can only select ONE shift per day.")
                continue
            else:             
                selected_day.append(available_day)
        
            # Prompt to choose shifts
            # Error handling for users input for shifts
            while True: 
                available_shift = input("Enter your available shift: ")
                if not check_valid_shift(available_shift):
                    pass
                else:
                    # If all conditions are met, start appending users' input 
                    with open(file_name, "a") as schedule_record:
                        writer = csv.writer(schedule_record)
                        writer.writerow([days_dict(7)[available_day], available_shift, " Added"])
                        schedule_record.close()
                    print(f'--> {days_dict(7)[available_day]} - {available_shift} is added to your roster.')
                    break

        # Return warning for invalid input if users' selection for days are not listed in Prompt 1 or not equal to "Q"
        else:
            print("--> Invalid input! Please try again.")




            