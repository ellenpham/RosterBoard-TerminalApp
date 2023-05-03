import colored
from colored import stylize

# Function for dislaying a warning of any invalid input
def invalid_input_message():
    warning = colored.fg("red") + colored.attr("bold")
    print(stylize("--> Invalid input! Please try again.", warning))

# Function for dislaying a warning of not listed selection
def selection_not_in_list():
    warning = colored.fg("red") + colored.attr("bold")
    print(stylize("--> Sorry your selection is not in the list!", warning))

# Function for styling notice lines
def notice_color():
    notice = colored.fg("green") + colored.attr("bold")
    return notice

# Function for styling warning lines
def warning_color():
    warning = colored.fg("magenta") + colored.attr("bold")
    return warning

# Function to check if users enter correct shifts
def check_valid_shift(shift):
    if shift == "AM" or shift == "PM" or shift == "Night":
        return True
    else:
        return False
    
