import os
import datetime

from datetime import timedelta
from Roster import Roster
from Item import Item
from common_functions import *


# Function for getting next week's Monday
def get_next_monday(week):
    today  = datetime.date.today()
    days_to_next_monday = week*7 - today.weekday()
    next_monday = today + datetime.timedelta(days = days_to_next_monday)
    return next_monday

# Function for putting days and their index in a dictionary
def get_days_dict(week):
    days_dict = dict()

    first_day = get_next_monday(week)

    for i in range(1,8):
        days_dict[f"{i}"] = first_day
        first_day = first_day + datetime.timedelta(days = 1)
    
    return days_dict

# Function for displaying a list of days for users selection
def display_weekday(days_dict):
    for i in range(1,8):
        day_str = days_dict[f"{i}"].strftime("%a %d/%m/%Y")
        print(f"[{i}] {day_str}")
    print("[Q] Enter Q to finish")


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
    os.system('clear')

    print(f'+{14*"-"}+')
    print("| AVAILABILITY |")
    print(f'+{14*"-"}+')

    # Start creating roster
    print("Enter index in the [] to select or enter Q to finish.")

    # Display list of day selection for the next ONE week
    days_dict = get_days_dict(1)
    display_weekday(days_dict)

    # Get users' input for building roster
    available_day = str()
    user_day_selection = True
    selected_day = []
    file_name = "schedule_record.csv"

    # Initialize roster object
    users_roster = Roster()

    # Start looping users for selection until they hit Q to quit
    while user_day_selection:
        available_day = input("Please select your available day: ")

        """
        user_day_selection = False in two cases:
        1. Three or more days (no duplication) were chosen before users hit Q
            --> Successfully created roster --> Back to Home Menu
        2. users choose two available days but do not want to continue to add more days 
            --> Any previous data are cleared, no roster --> Back to Home Menu
        
        """
        
        if (available_day == "Q"):
            # When users hit Q, count items in the roster list
            # If more than 3 days then users have completed creating roster

            if len(users_roster.roster) >= 3:
                user_day_selection = False
                users_roster.save_to_csv(file_name)
                print("-" * 130)
                print("\nTHANK YOU! You have completed your roster for the following week.")
                print("You have the option to view your roster again in the Home Menu.\n")
                print("-" * 130)
                print("\n")
                break

            # If less than 3 days, notify users of criteria for creating roster
            else: 
                print(stylize("--> You are required to be available for at least THREE days. Do you want to CONTINUE to select more days?", warning_color()))

                # Keep looping until users enter invalid answer
                # If yes, users are prompted back to continue add more days
                # If no, break out of main loop, no roster recorded
                while True:
                    continue_or_not = input(stylize(f"--> Enter 'Yes' to continue or 'No' to quit: ", warning_color()))
                    if continue_or_not == "No":
                        user_day_selection = False
                        print("-" * 110)
                        print("You have no roster for the following week.")
                        print("If you need further discussion, please contact our HR department on 1300 123 456.")
                        print("-" * 110)
                        break
                    elif continue_or_not == "Yes":
                        break
                    else:
                        invalid_input_message()

        # If a chosen day is in the days dictionary
        elif available_day in days_dict:
            # Check if the day is already chosen to prevent duplication
            if available_day in selected_day:
                print(stylize("--> Sorry you have selected this day! You can only select ONE shift per day.", warning_color()))
                continue
            else:             
                selected_day.append(available_day)
        
            # Shifts selection comes after a day is successfully chosen
            while True: 
                available_shift = input("Enter your available shift (AM, PM or Night): ")
                # If not valid shift input, keep looping
                if not check_valid_shift(available_shift):
                    invalid_input_message()
                # If valid shift input, the item is good to add to the roster list
                else: 
                    new_item = Item(days_dict[available_day], available_shift, action = "Added")
                    users_roster.roster.append(new_item)
                    day_str = days_dict[available_day].strftime("%a %d/%m/%Y")
                    print(stylize(f'--> {day_str} - {available_shift} is added to your roster.', notice_color()))
                    break

        # Invalid input if users' days selection is not listed or is not "Q"
        else:
            invalid_input_message()




            