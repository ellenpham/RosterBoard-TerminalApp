import os
import re

from create_roster_function import create_roster
from add_unavailability_function import add_unavailability

# Start the program with a welcome banner

print("+-----------*****-----------******----------*****----------*****----------*****----------*****----------*****-----------+")
print("|                                               WELCOME TO ROSTERBOARD                                                  |")
print("+                            A work scheduling platform for all rostered staff of NKG Corp.                             +")
print("|                        A centralized space to monitor your roster and put your schedule in place.                     |")
print("+------------*****-----------******----------*****----------*****----------*****----------*****----------*****----------+")
print("\n")
print("-------------------------------------------------------------------------------------------------------------------------")
print("Please note that every second Thursday, we will release a new request. Turn on the notification to receive the request.")
print("You are required to action your work schedule by 12pm on the Sunday of the same week.")
print("Please contact our HR department on 1300 123 456 if you have any questions.")
print("-------------------------------------------------------------------------------------------------------------------------")
print("\n")
print("Please hit Enter to move on to the the application instructions...")
input()

# Instructions
print("+------------+")
print("|INSTRUCTIONS|")
print("+------------+")
print("\n")
print("Once you Start the work schedule process, you will be prompted to action the below requests:")
print("- Create your roster for the following week.")
print("- Inform us your unavailability for the next ONE week after the following week.")
print("- Modify your schedule if needed.")
print("\n")
print("Are you ready to Start your work schedule? Please hit Enter to start...")
input()
os.system('clear')
print("-------------------------------------------------------------------------------------------------------------------------")

# Employee information

# Input name
def input_name():
    while True: 
        #Check if the string has any characters from a to z lower case, and A to Z upper case:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        user_first_name = re.findall(r"^[a-zA-Z]+$", first_name)
        user_last_name = re.findall(r"^[a-zA-Z]+$", last_name)

        if user_first_name and user_last_name:
            print(f'\nHello {first_name}, we hope you are doing good!')
            break
        else:
            print("Invalid input! Please try again.\n")
input_name()

print("\n")
# Department selection
def department_choice():
    print("Please select your department:")
    print("[1] Enter 1 for Operation")
    print("[2] Enter 2 for Inventory")
    print("[3] Enter 3 for Distribution")

    while True:
        try:
            department = int(input("Please enter your selection: "))
        except ValueError:
            print("Invalid input! Please try again.\n")
            continue

        if department != 1 and department != 2 and department != 3:
            print("Sorry, your selection is not in the list.\n")
            continue
        else:
            break
    
    if department == 1: 
        print("Operation")
    
    elif department == 2:
        print ("Inventory")
    else:
        print("Distribution")

department_choice()

print("-------------------------------------------------------------------------------------------------------------------------")

print("Let's start scheduling! Hit Enter to begin...")
input()
os.system('clear')


file_name = "schedule_record.csv"
ua_file_name = "ua_record.csv"

# File handling
# CSV file for store availability
try:
    roster_file = open(file_name, "r")
    roster_file.close()
    print("Record existed")

except FileNotFoundError as e:
    roster_file = open(file_name, "w")
    roster_file.write("Rostered days, Shifts, Actions\n")
    roster_file.close()
    print("Record is not existed, create records")

# CSV file for store unavailability
try:
    ua_file = open(ua_file_name, "r")
    ua_file.close()
    print("UA record existed")

except FileNotFoundError as e:
    ua_file = open(ua_file_name, "w")
    ua_file.write("Unavailable days, Shifts, Actions\n")
    ua_file.close()
    print("UA record is not existed, create records")
        

def main_menu():
    print("+-------------+")
    print("|  HOME MENU  |")
    print("+-------------+")

 
    # Start Home Menu selection 
    print("Please select your option: ")

    print("[1] Enter 1 to create your roster for the following week")
    print("[2] Enter 2 to add your unavailability for ONE week after the following week")
    print("[3] Enter 3 to view your current work schedule")
    print("[4] Enter 4 to modify your work schedule")
    print("[Exit] Enter Exit to exit the program")
    menu_choice = input("Enter your selection: ")
    return menu_choice

user_menu_choice = str()

while user_menu_choice != "Exit":
    user_menu_choice = main_menu()

    # Prompt 1
    if(user_menu_choice == "1"):
        create_roster(file_name)
    
    # Prompt 2
    elif(user_menu_choice == "2"):
        add_unavailability(ua_file_name)

    # Prompt 3
    elif(user_menu_choice == "3"):
        print("View roster")
    
    # Prompt 4
    elif(user_menu_choice == "4"):
        print("Modify roster")
    
    # Prompt 5
    elif(user_menu_choice == "Exit"):
        print("\n")
        print("+--------------------------------------------------------------------------------------------------+")
        print("| See you again! Make sure you action your work schedule before this Sunday to secure your roster. |")
        print("| Please contact our HR department on 1300 123 456 if you have any questions.                      |")
        print("+--------------------------------------------------------------------------------------------------+")
        print("\n")
        # clear data in csv file when exit program
        os.system("rm schedule_record.csv")
        os.system("rm ua_record.csv")
        continue
    
    else:
        print("Invalid input! Please try again.")