# def name():
#     while True:
#         user_name = input("Enter your name: ")
#         for i in [int]:
#             try:
#                 user = i(user_name)
#             except:
#                 pass
#             else:
#                 print("Invalid input!")
# name()

# print("continue")

# import re

# # name_input = input("Enter your name: ")

# while True: 
#     #Check if the string has any characters from a to z lower case, and A to Z upper case:
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")
#     user_first_name = re.findall(r"^[a-zA-Z]+$", first_name)
#     user_last_name = re.findall(r"^[a-zA-Z]+$", last_name)

#     if user_first_name and user_last_name:
#         print(f'Hello {first_name}, we hope you are doing good!')
#         break
#     else:
#         print("Invalid input! Please try again.")

# from datetime import datetime as dt
# now = dt.now()
 
# s = now.strftime("%A %d %m %-Y")
# print(s)

# from datetime import datetime, timedelta
# dt = datetime.now()
# td = timedelta(days=5)
# # your calculated date
# my_date = dt + td

# print(my_date)

# import datetime


# print((datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%A %B %d %-Y"))
# print((datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%A %B %d %-Y"))
# print((datetime.datetime.now() + datetime.timedelta(days=8)).strftime("%A %B %d %-Y"))
# print((datetime.datetime.now() + datetime.timedelta(days=9)).strftime("%A %B %d %-Y"))
# print((datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%A %B %d %-Y"))
# print((datetime.datetime.now() + datetime.timedelta(days=11)).strftime("%A %B %d %-Y"))
# print((datetime.datetime.now() + datetime.timedelta(days=12)).strftime("%A %B %d %-Y"))

# import datetime
 
# from datetime import timedelta 
 
# d=int(27)
# m=int(4)
# y=int(2023)
     
# # roster release date
# release_date = datetime.datetime(y, m, d) 

# # Monday to Sunday the following week
# # Monday
# mon = (release_date + timedelta(days = 4)).strftime("%A %B %d %-Y")
# print("[1]", mon) 

# # Tuesday
# tue = (release_date + timedelta(days = 5)).strftime("%A %B %d %-Y")
# print("[2]", tue) 

# # Wednesday
# wed = (release_date + timedelta(days = 6)).strftime("%A %B %d %-Y")
# print("[3]", wed) 

# # Thursday
# thu = (release_date + timedelta(days = 7)).strftime("%A %B %d %-Y")
# print("[4]", thu) 

# # Friday
# fri = (release_date + timedelta(days = 8)).strftime("%A %B %d %-Y")
# print("[5]", fri) 

# # Saturday
# sat = (release_date + timedelta(days = 9)).strftime("%A %B %d %-Y")
# print("[6]", sat) 

# # Sunday
# sun = (release_date + timedelta(days = 10)).strftime("%A %B %d %-Y")
# print("[7]", sun)

# # Finish choosing the days

# print("[Q] Finish your selection")


# def validate_entered_number(num):
#     """
#     Checks if the number is positive and is less or equal to 42.
#     Returns True if the number matches these conditions,
#     otherwise it returns False.
#     """
#     if num < 0:
#         print ("That is not a positive integer.")
#         return False

#     if num > 42:
#         print ("The number cannot exceed 42.")
#         return False

#     return True

# def main():
#     entered_numbers = []

#     while True:
#         try:
#             num = int(input("Enter a positive integer less or equal to 42: "))
#         except ValueError:
#             print ("You should enter a number")
#             continue
#         if validate_entered_number(num):
#             entered_numbers.append(num)
#             if sum(entered_numbers) > 179:
#                 print ("The sum of the numbers is %s" % sum(entered_numbers))
#                 print ("The smallest number entered is %s" % min(entered_numbers))
#                 print ("The largest number entered is %s" % max(entered_numbers))
#                 return

# if __name__ == "__main__":
#     main()

# import csv

# with open('file.csv', 'a') as f:
#     w = csv.writer(f, quoting=csv.QUOTE_ALL) 

# while (1):
#     why = input("why? ")
#     date = input("date: ")
#     story = input("story: ")
#     w.writerow([why, date, story])


# with open("hello.txt", "w") as my_file:
#     my_file.write("Hello world \n")
#     my_file.write("I hope you're doing well today \n")
#     my_file.write("This is a text file \n")
#     my_file.write("Have a nice time \n")

# with open("hello.txt") as my_file:
#     for line in my_file:
#         print(line)


# libraries
# import sys

# # list variable to store name
# names = []

# # limits to save name
# limit = 10

# # function to display menu
# def menu():
#     print("Enter 1 to add Name")
#     print("Enter 2 to show list")
#     print("Enter 3 to quit")
#     choice = int(input("Enter your choice : "))
#     return choice

# # running for infinite times till user quits
# while(True):
#     choice = menu()
#     if(choice == 1):
#         name = input("Enter name to add in list : ")
#         if(len(names) >= 1):
#             print("You cannot enter more names")
#         else:
#             names.append(name)
#             print(name + " - Name saved successfully.")
#     if(choice == 2):
#         print("List of names : ")
#         print(names)
#     if(choice == 3):
#         sys.exit()


# import pandas as pd

# df = pd.read_csv('test_file.csv', sep=', ', engine='python')

# new_df = df[['min-zoom','max-zoom']].drop_duplicates()

# new_df.to_csv('out.csv', index=False)


# originalFile = open('schedule_record.csv','r')

# finalFile = open('schedule_record_filtered.csv','w')

# listRows = []

# for row in originalFile:

#     if row in listRows:
#         continue

#     else:
#         finalFile.write(row)
#         listRows.append(row)
