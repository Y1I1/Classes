# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os

from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    run = True 
    while run:

        new_username = input("New Username: ")

        if new_username in username_password.keys():
            print('This username already exists')
            break
            
        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}") #writes in the username and password like 'usernme;password' in the user.txt file
                out_file.write("\n".join(user_data))
            run = False
        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match") 

def add_task():

    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    while True: #contained in a while loop since even though the user doesnt exist it doesnt prompt the user to add another username, instead it makes a task with a random username anyway
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break
        

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs)) #creates a string with the information from the task_list dict
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():

    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str) 

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    '''
    print()
    index = []
    count = 1 #created a counter to display next to the task name order so the user can select the specific task
    for t in task_list:
        if t['username'] == curr_user:
            index.append(task_list.index(t)) #adds all the indexes of the user specific tasks to an index list
            disp_str = f"Task {count}: \t\t {t['title']}\n"

            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            count+=1
    option = int(input('''Enter the Task number you wish to select, 
or enter '-1' to return to menu: ''')) #asks the user to choose a task displayed
    #print(index)
    for i in index: #loops through the indexes of the user specific task and checks to see if the index numbber +1 = the number the user chose
        #print(i)
        #print(index.index(i))
        if option == index.index(i)+1: #selects the specific task e.g task 1 (= index 0), task 2 (= index 1)
            print (task_list[i]['username']) #print the username #could usse print curr_user aswell
            action = int(input('''would you like to: 
    1) edit or 
    2) mark work as complete?
    : ''')) 
            if action == 2: #if the user chose 2 it will change the specific task to = True in the dictionary 
                task_list[i]['completed'] = True
                #print(task_list[i]['completed']) check
                print('your task has been marked as completed') #outputs a message so we know the action has been completed

            elif action == 1 and task_list[i]['completed'] == False: #checks if action is 1 and if the specific task has not been completed
                edit = int(input('''would you like to: 
    1) change the user this task was assigned to or 
    2) change its due date?
    : '''))
                if edit == 1:
                    user_check = []
                    for x in task_list:
                        print(x['username']) 
                        user_check.append(x['username'])

                    while True: #checks if the person the user wants to assign the task to exists.
                        user_change = input('type a user from those list of users above to change the task to: ')
                        if user_change in user_check: # if the user exists update the assigned user 
                            task_list[i]['username'] = user_change
                            print(task_list[i]['username'])
                            print(f'the user has been updated to {user_change}') #displays a message to verify the action is complete 
                            break
                        else:
                            print('that user does not exist please try again ') #displays an error message if the user doesnt exist
                    

                elif edit == 2: #if the user enters 2 then the program will display the tasks due date and the user to chnage it based on the format provided
                    print('the due date is: ')
                    print(task_list[i]['due_date'])
                    while True: #prompts the user to input a date in the correct format 
                        try:
                            task_due_date = input("New due date of task (YYYY-MM-DD): ")
                            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                            break

                        except ValueError:
                            print("Invalid datetime format. Please use the format specified") #displays an error message of the format isnt correct 

                    task_list[i]['due_date'] = due_date_time #updating the tasks due date
                    print(task_list[i]['due_date'])
                    print(f'your due date has been changed to {due_date_time}') #verification messages
            
            elif option == -1: #allows the user to go back to the main menu (breaks the loop if option is -1)
                pass

def generate_report():
    print('generating your report now...\n') #prints a message for the user


    #creates a file called task_overview.txt
    with open("task_overview.txt", "w") as f:
        global number_of_tasks
        number_of_tasks = 0

        completed = 0
        uncomplete = 0
        for i in task_list:
            number_of_tasks +=1
            if i['completed'] == True:
                completed +=1
            else:
                uncomplete += 1
            


        f.write(f'the number of tasks in the task manager is: {number_of_tasks} \n')
        f.write(f'the number of completed tasks in the task manager is: {completed}\n')
        f.write(f'the number of uncompleted tasks in the task manager is: {uncomplete}')

    print('your report has been generated please check the task_overview.txt file for your report')

    with open("user_overview.txt", "w") as f:
        number_of_users = 0
        users = []
        number_of_tasks = 0

        for i in task_list:
            if i['username'] not in users:
                number_of_users += 1
                users.append(i['username'])

        f.write(f'total number of users registered in task manager: {number_of_users}\n')
        

        for x in users:
            count = 0
            completed = 0
            uncompleted = 0
            overdue = 0
            for t in task_list:
                #print(type(t['due_date'])) check
                #print(t['due_date']) check
                if t['username'] == x:
                    count +=1
                    if t['completed'] == True:
                        completed +=1

                    elif datetime.now() > t['due_date'] and t['completed'] == False: #comparing the current date with the due date and incrementing overdue tasks if the current date is larger than the due date
                        overdue += 1

                    else:
                        uncompleted += 1
            number_of_tasks += count 
                            
            percentage_total = count/number_of_tasks *100
            percentage_completed = completed/count * 100
            percentage_uncompleted = uncompleted / count * 100
            percentage_overdue = overdue/uncompleted* 100 if uncompleted != 0 else 0 #inline if statement to check if uncompleted is not 0 if so percentage is set to 0
            f.write(f'''USER {x}:
TOTAL TASKS:    |PERCENTAGE OF ALL TASKS ASSIGNED TO THE USER:   |PERCENTAGE OF COMPLETED TASKS:  |PERCENTAGE OF UNCOMPLETED TASKS:   |PERCENTAGE OF OVERDUE TASKS: 
{count}                 {percentage_total}%                                            {percentage_completed}%                               {percentage_uncompleted}%                                     {percentage_overdue}%\n''')
#making the information look nice and outputting un a user friendly manner
        f.write(f'total number of tasks tracked in task manager: {number_of_tasks}')        

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generates report for tasks and users
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
       view_all()
            
    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr':
        generate_report()

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------\n")

        #displays both overview files in the terminal 

        with open('task_overview.txt', 'r+') as f:
            for line in f:
                print(line)
        print()
        with open('user_overview.txt','r+') as f:
            for line in f:
                print(line) 

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made an invalid choice, Please Try again")