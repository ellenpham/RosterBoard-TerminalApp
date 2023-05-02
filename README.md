# **My Pham - T1A3 - Terminal Application**

# References

# Links
1. GitHub repository:
2. Presentation:
3. Project management plan:

# Code style guide and styling conventions

1. Rossum, G., Warsaw, B., Coghlan, N. (2001) PEP8 - Style Guide for Python Code [Styling Convention]. https://peps.python.org/pep-0008/

2. Goodger, D., Rossum, G. (2001) PEP 257 - Docstring Conventions [Styling Convention]. https://peps.python.org/pep-0257/

# Functionalities

## Description

NKG Corp. is a warehousing and distribution company. They have a large number of staff working across rotating shifts. **RosterBoard** is an internal application that allows company staff to provide their availability and unavailability in the two weeks time, which are used for roster building and workforce planning. 


## Main features
1. Users (the company staff) are asked to provide their name and their department before starting their work schedule. If all answers are valid, they get prompted to the Home Menu. 
2. The Home Menu has 5 prompts : Create Roster, Add Future Unavailability, View Roster, Modify Roster and Exit Program. 
3. In the Create Roster Function, users are requested to create their roster for the following week based on a list of questions:
    - Select available days for the following week (Monday to Sunday).
    - Select available shifts for the chosen day.

    There are some criterias when creating the roster. First, if available days are less than THREE days, users are required to select more days, if not, they have no roster for the following week and prompted back to Home Menu. Second, users can only choose ONE shift per available day. 

4. In the Add Future Unavailability Function, users are requested to  select their unavailable days for the ONE week after the following week. Here they can input as many days or shifts as they wish. If they have no unavailability, there will be no record.  

5. In the View Roster Function, users' final work schedule is displayed. Users can confirm this work schedule or if they change their mind, they can have option to modify the current schedule. Note that once users finish providing their availability and unavailability in the last two functions, they can not go back and restart the procedure. They can only modify the schedule records by using Modify Roster Function. 

6. In the Modify Roster Function, users have two options.

    - Modify the current roster: options include changing shift, removing a current day or adding a new day. 
    - Modify unavailability: users will have to redo their unavailability from the scratch if they do not wish to keep their current record. 

## Control Flow Diagram

The below diagram illustrates how the flow of data and the application's logic. 

![Control Flow Diagram](./docs/RosteringApp_ControlFlowDiagram.png)
(Diagram created using diagram.net.io)

<br>

# Implementation Plan

### Overall implementation process

1. The project management plan is outlined with the kanban board format using Trello.

2. Created a control flow diagram to visualize the flow of data in the app. The diagram was slightly modified along the way due to little compromised changes in the development process. 

3. Created a mock output using notepad to help visualizing the expected output when the app is run successfully and without errors. 

4. Start writing the source code. Define a range of `Classes`, `Functions`, `Modules` and `Methods` used for each listed feature. 

5. Errors were handled along the way during the coding process.

6. Develop a testing plan, including manual tests and tests using `pytest`.

7. Write scripts for app execution and develop help documentation. 

8. Readme file was updated along the way whenever a task was finished.  

9. Summarise the project with slide deck and presentation 

<br>

### The development of each feature and timeline. 

The development steps are listed as below:

1. Getting users' information
2. Create Roster Function
3. Add Future Unavailability Function
4. View Roster Function
5. Modify Roster Function
6. Test cases
7. Write scripts

<br>

**Getting users' information**

This section includes getting users' input for their name and their department. This section is included in `main.py` file. The `main.py` file also include a section for Home Menu, which use `while` loop with `if` `elif` `else` to keep prompting users back to Home Menu after each completed task. Main classes and functions are arranged in separated files and get imported in the `main.py` file for modularised purpose.

<table>
    <thead>
        <tr>
            <th>Checklist</th>
            <th>Items</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</th>
            <td>A function to return users' name</th>
            <td>25-26 Apr</th>
        </tr>
        <tr>
            <td>2</th>
            <td>Error handling: name input must be all letters, using `re` module</th>
            <td>25-26 Apr</th>
        </tr>
        <tr>
            <td>3</th>
            <td>A function to return users's department</th>
            <td>25-26 Apr</th>
        </tr>
        <tr>
            <td>4</th>
            <td>Error handling: department selection must be in the given list, using `try` `except`</th>
            <td>25-26 Apr</th>
        </tr>
        <tr>
            <td>5</th>
            <td>A greeter is displayed once users finish registering, followed by the Home Menu</th>
            <td>25-26 Apr</th>
        </tr>
        </tr>
        <tr>
            <td>6</th>
            <td>Home Menu is displayed with FIVE main prompts</th>
            <td>25-26 Apr</th>
        </tr>
    </tbody>
</table>


**Day 1**: Create project management plan, design control flow diagram, create mocking output, create welcome banner, introduction and instructions, research on `datetime` module, start on functions to get users' information.

![Trello_Day1_1](./docs/Trello_Day1_1.png)
![Trello_Day1_2](./docs/Trello_Day1_2.png)

<br>

**Create Roster Function**

This section allows users to choose their available days during the following week. Users are required to choose more than THREE days of work and only ONE shift per day. Their inputs will be used to form their roster.

<table>
    <thead>
        <tr>
            <th>Checklist</th>
            <th>Items</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</th>
            <td>A function that always returns dates for Mon to Sun of the following week using `weekday()`</th>
            <td>26-28 Apr</th>
        </tr>
        <tr>
            <td>2</th>
            <td>User's chosen days get recorded in csv file using `csv.writer`</th>
            <td>26-28 Apr</th>
        </tr>
        <tr>
            <td>3</th>
            <td>Checking list of input to make sure a chosen day can not be selected again </th>
            <td>26-28 Apr</th>
        </tr>
        <tr>
            <td>4</th>
            <td>Use `while` to looping users to keep selecting days until they hit Q to end</th>
            <td>26-28 Apr</th>
        </tr>
        <tr>
            <td>5</th>
            <td>Using `csv.reader` and using `len()` to count if users select less than 3 days. If yes, prompt to add more days. If not, users have no roster, clear all input in csv file using `csv.writer`</th>
            <td>26-28 Apr</th>
        </tr>
        <tr>
            <td>6</th>
            <td>A function to check valid shift input and make sure only ONE shift is selected</th>
            <td>26-28 Apr</th>
        </tr>
        <tr>
            <td>7</th>
            <td>Using `len()` to check existed record in csv file. If existed, prompt users to Modify Roster Function if they need to make changes</th>
            <td>26-28 Apr</th>
        </tr>
    </tbody>
</table>


**Day 2**: Complete functions for getting users' information, start working on Create Roster Function, research on OOP, research on file handling and `csv` module, research on `RegEx`.

![Trello_Day2_2](./docs/Trello_Day2_2.png)
![Trello_Day2_3](./docs/Trello_Day2_3.png)

<br>

**Day 3**: Complete Create Roster Function and start reporting on Readme file, start working on Add Future Unavailability Function. 

![Trello_Day3_1](./docs/Trello_Day3_1.png)
![Trello_Day3_2](./docs/Trello_Day3_2&3.png)

<br>

**Add Future Unavailability Function**

This section allows users to choose their unavailable days during week after the following week. Users can choose as many days and shifts as they wish and they all get record as their unavailability request.

<table>
    <thead>
        <tr>
            <th>Checklist</th>
            <th>Items</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</th>
            <td>Unavailability records are stored in a separate CSV file </th>
            <td>28-29 Apr</th>
        </tr>
        <tr>
            <td>2</th>
            <td>Users can not select two same days but can select more than one shift, using `list.append()` to allow multiple shifts </th>
            <td>28-29 Apr</th>
        </tr>
        <tr>
            <td>3</th>
            <td>Chosen shifts are stored in `set()` to eliminate duplication </th>
            <td>28-29 Apr</th>
        </tr>
        <tr>
            <td>4</th>
            <td>If users accidently select a day but no shift is chose. The chosen day will not be counted as their unavailable day, using `len()` to check set items</th>
            <td>28-29 Apr</th>
        </tr>
        <tr>
            <td>5</th>
            <td>Error handling for all users' input using `while` loop and `if` `elif` `else`</th>
            <td>28-29 Apr</th>
        </tr>
        <tr>
            <td>6</th>
            <td>Using `len()` to check existed record in csv file. If existed, prompt users to Modify Roster Function if they need to make changes</th>
            <td>28-29 Apr</th>
        </tr>
    </tbody>
</table>

<br>

**View Roster Function**

This section allows users to view their work schedule which has been recorded from their previous inputs. Their final work schedule includes users' name, department, action date, followed by their rostered days and unavailability records.

<table>
    <thead>
        <tr>
            <th>Checklist</th>
            <th>Items</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</th>
            <td>Users' name, department and action date are displayed by importing from `main.py` </th>
            <td>29 Apr</th>
        </tr>
        <tr>
            <td>2</th>
            <td>Users' input for availability and unavailability are arranged in a table format using `prettytable`</th>
            <td>29 Apr</th>
        </tr>
        <tr>
            <td>3</th>
            <td>A prompt to request users to confirm their current work schedule</th>
            <td>29 Apr</th>
        </tr>
        <tr>
            <td>4</th>
            <td>If users do not confirm, they are prompted back to Home Menu and choose Modify Roster Function</th>
            <td>29 Apr</th>
        </tr>
        <tr>
            <td>5</th>
            <td>Error handling for users' input using `while` loop and `if` `elif` `else`</th>
            <td>29 Apr</th>
        </tr>
    </tbody>
</table>


Day 4: Complete Add Future Unavailability Function and View Roster Function

![Trello_Day4_1](./docs/Trello_Day4_1.png)
![Trello_Day4_2](./docs/Trello_Day4_2.png)

<br>

**Modify Roster Function**

This section allows user to modify their current roster or modify their current unavailability records. 
1. Modify current roster: Here users have options to modify the shift of a current rostered day, to remove a current rostered day or to add a new day to the roster. 

2. Modify current unavailability records: the initial idea is to allow users manipulate the records in the same way as above. Later on, I decided to simplify it by prompting users to redo their unavailability from the scratch.

<table>
    <thead>
        <tr>
            <th>Checklist</th>
            <th>Items</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</th>
            <td>Prompt users to two options: 1/ Modify their current roster or 2/ Modify their unavailability record</th>
            <td>30 Apr - 02 May</th>
        </tr>
        <tr>
            <td>2</th>
            <td>User have three options on how they can manipulate their current roster: 1/to modify, 2/to remove and 3/to add</th>
            <td>30 Apr - 02 May</th>
        </tr>
        <tr>
            <td>3</th>
            <td>Requirement when adding a day: if the day is already existed --> have to choose another day.</th>
            <td>30 Apr - 02 May</th>
        </tr>
        <tr>
            <td>4</th>
            <td>Requirement when modifying or removing a day: if the day is not existed --> have to choose another day</th>
            <td>30 Apr - 02 May</th>
        </tr>
        <tr>
            <td>5</th>
            <td>Requirement when removing a day: re-check if there are less than THREE rostered days, using `csv.reader` and `len()` to read and count</th>
            <td>30 Apr - 02 May</th>
        </tr>
         <tr>
            <td>6</th>
            <td>Error handling for users input: inputs for any modified days need to be in a given format, using `strptime()`</th>
            <td>30 Apr - 02 May</th>
        </tr>
         <tr>
            <td>7</th>
            <td>A function for checking valid shifts input to reuse whenever users are required to input their shifts</th>
            <td>30 Apr - 02 May</th>
        </tr>
         <tr>
            <td>8</th>
            <td>Prompt users to redo their unavailability by importing `add_unavailability()` function</th>
            <td>30 Apr - 02 May</th>
        </tr>
    </tbody>
</table>

Day 5: Work on Modify Roster Function 
![Trello_Day5_1](./docs/Trello_Day5_1.png)
![Trello_Day5_2](./docs/Trello_Day5_2.png)

to be continued...