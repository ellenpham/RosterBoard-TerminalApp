import os
import datetime

from datetime import timedelta
from Roster import Roster
from Item import Item
from common_functions import *


# Function using weekday() method and datetime.timedelta() to always get next week's Monday
def get_next_monday(week):
    today  = datetime.date.today()
    days_to_next_monday = week*7 - today.weekday()
    next_monday = today + datetime.timedelta(days = days_to_next_monday)
    return next_monday

# Create a dictionation for weekdays
def get_days_dict(week):
    days_dict = dict()

    first_day = get_next_monday(week)

    for i in range(1,8):
        days_dict[f"{i}"] = first_day
        first_day = first_day + datetime.timedelta(days = 1)
    
    return days_dict

# display a list of weekdays
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

    days_dict = get_days_dict(1)
    display_weekday(days_dict)

    
    # Get users' input for building roster
    available_day = str()
    user_day_selection = True
    selected_day = []
    file_name = "schedule_record.csv"

    # Initialize roster object
    users_roster = Roster()

    while user_day_selection:
        available_day = input("Please select your available day: ")

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

            if len(users_roster.roster) >= 3:
                user_day_selection = False
                users_roster.save_to_csv(file_name)
                print("-" * 130)
                print("\nTHANK YOU! You have completed your roster for the following week.")
                print("You have the option to view your roster again in the Home Menu.\n")
                print("-" * 130)
                print("\n")
                break

        
            else: # if less than 3 available days, users can choose to continue adding more days or have no roster at all
                print(stylize("--> You are required to be available for at least THREE days. Do you want to CONTINUE to select more days?", warning_color()))
                # Error handling for users input for continue-or-not prompt
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

        elif available_day in days_dict:
            # Restrict users' selection of 2 same days. 
            if available_day in selected_day:
                print(stylize("--> Sorry you have selected this day! You can only select ONE shift per day.", warning_color()))
                continue
            else:             
                selected_day.append(available_day)
        
            # Prompt to choose shifts
            # Error handling for users input for shifts
            while True: 
                available_shift = input("Enter your available shift (AM, PM or Night): ")
                if not check_valid_shift(available_shift):
                    invalid_input_message()
                else: 
                    new_item = Item(days_dict[available_day], available_shift, action = "Added")
                    users_roster.roster.append(new_item)
                    day_str = days_dict[available_day].strftime("%a %d/%m/%Y")
                    print(stylize(f'--> {day_str} - {available_shift} is added to your roster.', notice_color()))
                    break

        # Return warning for invalid input if users' selection for days are not listed in Prompt 1 or not equal to "Q"
        else:
            invalid_input_message()




            