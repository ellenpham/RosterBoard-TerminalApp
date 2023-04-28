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

# print ('screen question1 here')
# screen1 = input('user answer')
# if screen1 == 'yes':
#     print('screen question2 here')
#     screen2 = input('user answer')
#     if screen2 == 'yes':
#         print('screen question3 here')
#         screen3 = input('user answer')
#     else:
#         print('camera question1 here')
#         camera1 = input('user answer')
# else:
#     print('battery question1 here')
#     battery1 = input('user answer')
#     if battery1 == 'yes':
#         print('battery question2 here')
#         battery2 =input('user answer')
#     else:
#         print('wifi question1 here')
#         wifi1 = input('user answer')

# import csv

# with open('test_file.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# import csv

# reader = csv.reader(open("employees.csv"))
# no_lines= len(list(reader))
# print(no_lines)

# import random
# correct = 0
# incorrect = 0
# usedwords = []
# print ('Welcome to text twist, you have 14 guesses to get 7 words made up of 4, 5 or 6 letters. Good Luck!')

# for i in range(14):
#     print ("Your letters are 'E' 'P' 'L' 'B' 'E' 'B', what is your guess?")
#     answer = input()
#     if answer in usedwords:
#         print ("Sorry, you've already used this word")
#     else: #Newly added
#         usedwords.append(answer) #We have to add the input words to the list if they are new
#         if answer == 'belle' or answer == 'bleep' or answer == 'pebble' or answer == 'beep' or answer == 'bell' or answer == 'peel' or answer == 'peep':
#             if answer in usedwords:
#                 print ('Nice that was one of the words!')
#             usedwords.append(answer)
#             correct = correct + 1
#         if answer != 'belle' and answer != 'bleep' and answer != 'pebble' and answer != 'beep' and answer != 'bell' and answer != 'peel' and answer != 'peep':
#             print ('Sorry, that was not one of the words.')
#             incorrect = incorrect + 1


# print ('Your final score was'), correct, 'correct and', incorrect, 'wrong.'


    # Remove duplicates in schedule_record.csv file if there's any
    # original_file = open('schedule_record.csv','r')

    # final_file = open('schedule_record_filtered.csv','w')

    # list_rows = []

    # for row in original_file:

    #     if row in list_rows:
    #         continue

    #     else:
    #         final_file.write(row)
    #         list_rows.append(row)
    
    # original_file.close()
    # final_file.close()

