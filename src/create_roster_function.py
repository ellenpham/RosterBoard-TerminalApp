import datetime
from datetime import timedelta
import csv

def create_roster(file_name):
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("You are about to create your roster for next week...")
    print("\n")
    print("**Important note**")
    print("\n")
    print("You are required to be available for at least THREE days.")
    print("If you select less than THREE days of work, you will not get rostered.")
    print("If you select THREE days or more, you will get rostered for all of the available days that you have chosen.")
    print("You can only select ONE available shift, shift duration is 5 hours, anything over will get counted to your overtime rate.")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Hit enter to start...")
    input()

    print("+--------------+")
    print("| AVAILABILITY |")
    print("+--------------+") 

    # Start creating roster
    print("Enter index in the [] to select or enter 8 to finish.")

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
    print("[8] Enter 8 to finish your selection\n")

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

    while user_day_selection:
        available_day = input("Please select your available days: ")

        if (available_day == "8"):
            # count data from csv file to check how many available days get recorded
            # if more than 3 available days then users have completed creating roster
            csv_reader = csv.reader(open("schedule_record.csv"))
            line_count = len(list(csv_reader))
            if line_count >= 4:
                user_day_selection = False
                print("\nThank you! You have completed your roster for the following week.\n")
                print("-------------------------------------------------------------------------------------------------------------------------\n")
                break
           

            else: # if less than 3 available days, users can choose to continue adding more days or have no roster at all
                print("Your available days are less than 3 days. Do you want to continue to select more days?")
                continue_or_not = input ("Enter Yes to continue or No to quit: ")
                if continue_or_not == "No":
                    user_day_selection = False
                    print("---------------------------------------------------------------------------------")
                    print("You have no roster for the following week.")
                    print("If you need further discussion, please contact our HR department on 1300 123 456.")
                    print("-------------------------------------------------------------------------------- ")
                    break
                

        elif available_day in days_dict:
            # Prompt to choose shifts
            available_shift = input("Enter your available shifts (AM, PM or Night): ")
            with open(file_name, "a") as schedule_record:
                writer = csv.writer(schedule_record)
                writer.writerow([days_dict[available_day], available_shift, " Added"])
            print(f'{days_dict[available_day]} - {available_shift} is added to your roster.')

        else:
            print("Invalid input! Please try again.")


    # Remove duplicates in schedule_record.csv file if there's any
    original_file = open('schedule_record.csv','r')

    final_file = open('schedule_record_filtered.csv','w')

    list_rows = []

    for row in original_file:

        if row in list_rows:
            continue

        else:
            final_file.write(row)
            list_rows.append(row)
    
    original_file.close()
    final_file.close()


        