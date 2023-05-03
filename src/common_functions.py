import colored
from colored import stylize

# Functions for coloring 
def invalid_input_message():
    warning = colored.fg("red") + colored.attr("bold")
    print(stylize("--> Invalid input! Please try again.", warning))

def selection_not_in_list():
    warning = colored.fg("red") + colored.attr("bold")
    print(stylize("--> Sorry your selection is not in the list!", warning))

def notice_color():
    notice = colored.fg("green") + colored.attr("bold")
    return notice

def warning_color():
    warning = colored.fg("magenta") + colored.attr("bold")
    return warning


# Function to check if user put in correct shifts
def check_valid_shift(shift):
    if shift == "AM" or shift == "PM" or shift == "Night":
        return True
    else:
        return False