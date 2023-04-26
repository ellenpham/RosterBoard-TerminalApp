# My Pham - T1A3 - Terminal Application 

## References

## Links
1. GitHub repository:
2. Presentation:
3. Project management plan:

## Code style guide and styling conventions

1. Rossum, G., Warsaw, B., Coghlan, N. (2001) PEP8 - Style Guide for Python Code [Styling Convention]. https://peps.python.org/pep-0008/

## Functionalities

**Description**

NKG Corp. is a warehousing and distribution company. They have a large number of staff working across rotating shifts. **RosterBoard** is an application that help the company collect the availability and unavailability from rostered staff in order to prepare the workforce plan. The application also allows the staff to view their upcoming roster and flexibly schedule their work. 


**Main features**
1. Users (the company staff) are asked to provide their name and their department before starting their work schedule. If all answers are valid, they can move on to the main menu. 
2. The main menu has 5 prompts : Create roster, Add unavailability, View roster, Modify Roster and Exit program. 
3. In the Create Roster function, users are requested to create their roster for the following week based on a list of questions:
    - Choose their available days for the following week (Monday to Sunday).
    - Choose their available shifts for the chosen day.

    There are a few criterias when creating the roster. First, if the numbers of available day is less than THREE days, users will be prompted to choose 1 more available day or if they can not provide more days, they will be informed that they have no roster for the following week and the program ends here. Second, users can only choose ONE shift per available day. 

4. In the Add Unavailability function, users are requested to manually input their unavailability for ONE week after the following week according to a given format. Here they can input as many days or shifts as they wish to be their unavailability. If they have no unavailability, this will not get recorded. 

5. In the View Roster function, users' final work schedule is displayed, including staff name, department, the roster for the following week and unavailable days for the week after the following week. Users can confirm if the work schedule is correct or they can change their schedule, in which users will be prompted to the next function.

6. In the Modify Roster function, users can change their availability/unavailability if they change their mind, these modified information will get updated in their final roster and users can go back to the Main Menu to view the modified schedule.

working in progress...