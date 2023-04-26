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

import datetime
 
from datetime import timedelta 
 
d=int(27)
m=int(4)
y=int(2023)
     
# roster release date
release_date = datetime.datetime(y, m, d) 

# Monday to Sunday the following week
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

# Finish choosing the days

print("[Q] Finish your selection")

