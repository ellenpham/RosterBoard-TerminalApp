from prettytable import from_csv
from common_functions import *
import os

# Main function to view full work schedule
def view_schedule():
    
    # Display roster for the following week 
    print("\nRoster for the following week: \n")
    with open('schedule_record.csv') as table_file:
        roster_tab = from_csv(table_file)
        table_file.close()
    print(roster_tab)

    # Display unavailability records for the week after the following week
    print("\nUnavailability record: \n")
    with open('ua_record.csv') as ua_table_file:
        ua_tab = from_csv(ua_table_file)
        table_file.close()
    print(ua_tab)

    print("\n")

    # Prompt users to confirm or modify the work schedule
    print("-" * 130)
    print("If you are happy with the above work schedule, please enter 'Yes' to confirm or 'No' if you wish to make changes.")
    while True: 
        confirm_or_not = input("Would you like to confirm your work schedule? ")
        if confirm_or_not == "Yes": 
            print("\n")
            print(f'+{"-"*126}+')
            print(f'|{16*" "}Thank you for your coorporation! You have completed your work schedule for the next two weeks!{16*" "}|')
            print(f'+{"-"*126}+')
            print("\n")
            break

        elif confirm_or_not == "No":
            print("\n")
            print(stylize("You have the option to modify your work schedule. Please keep following the prompts.", notice_color()))
            print("\n")
            break

        else:
            invalid_input_message()


    



