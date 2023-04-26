import datetime
from datetime import timedelta
import csv


def create_roster(file_name):
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("You are about to create your roster for next week...")
    print("\n")
    print("**Important note**")
    print("\n")
    print("You are required to be available at least 3 days. If you select less than 3 days of work, you will not get rostered.")
    print("If you select 3 or more days, you will get rostered for all of the available days that you have chosen.")
    print("You can only select 1 available shift, shift duration is 5 hours, anything over will get counted to your overtime rate.")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Hit enter to start...")
    input()

    print("----------------")
    print("| AVAILABILITY |")
    print("----------------")

    # Start selection
    print("Enter index in the [] to select or enter Q to finish.")

    d=int(11)
    m=int(5)
    y=int(2023)
        
    # roster release date
    release_date = datetime.datetime(y, m, d) 

    # Monday to Sunday of the following week
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
    print("[Q] Finish your selection")

    # user_available_day = str()

    # while user_available_day != "Q":
    #     user_available_day = create_roster(file_name)
        
    available_day = input("Please select your available days: ")
    with open(file_name, "a") as schedule_record:
        writer = csv.writer(schedule_record)

        if available_day == "1":
            writer.writerow([mon, " Added"])
            print(f'{mon} is added to your roster.')

        elif available_day == "2":
            writer.writerow([tue, " Added"])
            print(f'{tue} is added to your roster.')

        elif available_day == "3":
            writer.writerow([wed, " Added"])
            print(f'{wed} is added to your roster.')

        elif available_day == "4":
            writer.writerow([thu, " Added"])
            print(f'{thu} is added to your roster.')

        elif available_day == "5":
            writer.writerow([fri, " Added"])
            print(f'{fri} is added to your roster.')

        elif available_day == "6":
            writer.writerow([sat, " Added"])
            print(f'{sat} is added to your roster.')

        elif available_day == "7":
            writer.writerow([sun, " Added"])
            print(f'{sun} is added to your roster.')

        elif available_day == "Q":
            print("You have completed your roster for the following week.")

        else:
            print("Invalid input! Please try again.")

    print("-------------------------------------------------------------------------------------------------------------------------\n")