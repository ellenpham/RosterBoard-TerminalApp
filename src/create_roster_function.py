import datetime
from datetime import timedelta
import csv 

def create_roster(file_name):
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("You are about to create your roster for the following week...")
    print("\n")
    print("**Important note**")
    print("\n")
    print("You are required to be available for at least THREE days.")
    print("If you select less than THREE days of work, you will have no roster for the following week.")
    print("If you select THREE days or more, you will get rostered for all of the available days that you have chosen.")
    print("You can only select ONE available shift, shift duration is 5 hours, anything over will get counted to your overtime rate.")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Hit enter to start...")
    input()

    print("+--------------+")
    print("| AVAILABILITY |")
    print("+--------------+") 

    # Start creating roster
    print("Enter index in the [] to select or enter Q to finish.")

    # Roster release date
    d=int(25)
    m=int(5)
    y=int(2023)
        
    release_date = datetime.datetime(y, m, d) 

    # Monday to Sunday of the following week based on roster release date
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

    # Finish creating roster
    print("[Q] Enter Q to finish your selection\n")

    days_dict = {
        "1": mon,
        "2": tue,
        "3": wed,
        "4": thu,
        "5": fri,
        "6": sat,
        "7": sun,
    }    

    # Get users input
    available_day = str()
    user_day_selection = True
    selected_day = []

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
            # count data from csv file to check how many available days get recorded
            # if more than 3 available days then users have completed creating roster
            csv_reader = csv.reader(open("schedule_record.csv"))
            line_count = len(list(csv_reader))
            if line_count >= 4:
                user_day_selection = False
                print("\nTHANK YOU! You have completed your roster for the following week.")
                print("You have the option to view your roster again in the Home Menu.\n")
                print("-------------------------------------------------------------------------------------------------------------------------\n")
                break
           

            else: # if less than 3 available days, users can choose to continue adding more days or have no roster at all
                print("--> You are required to be available for at least THREE days. Do you want to CONTINUE to select more days?")
                # Error handling for users input for continue-or-not prompt
                while True:
                    continue_or_not = input ("--> Enter Yes to continue or No to quit: ")
                    if continue_or_not == "No":
                        user_day_selection = False
                        print("---------------------------------------------------------------------------------")
                        print("You have no roster for the following week.")
                        print("If you need further discussion, please contact our HR department on 1300 123 456.")
                        print("-------------------------------------------------------------------------------- ")
                        break
                    elif continue_or_not == "Yes":
                        break
                    else:
                        print("Invalid input! Please try again.")

        elif available_day in days_dict:
            # Restrict users' selection of 2 same days. 
            if available_day in selected_day:
                print("--> Sorry you have selected this day! You can only select ONE shift per day.")
                continue
            else:             
                selected_day.append(available_day)
           
            # Prompt to choose shifts
            # Error handling for users input for shifts
            while True:
                available_shift = input("Enter your available shifts (AM, PM or Night): ")
                if available_shift == "AM" or available_shift == "PM" or available_shift == "Night":
                    break
                else:
                    print("Invalid input! Please try again.")

            with open(file_name, "a") as schedule_record:
                 writer = csv.writer(schedule_record)
                 writer.writerow([days_dict[available_day], available_shift, " Added"])
            print(f'--> {days_dict[available_day]} - {available_shift} is added to your roster.')

        else:
            print("--> Invalid input! Please try again.")




        