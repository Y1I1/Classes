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
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

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
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        

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
    with open("Classes/21/tasks.txt", "w") as task_file:
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
            task_list_to_write.append(";".join(str_attrs))
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
    count = 1
    for t in task_list:
        if t['username'] == curr_user:
            index.append(task_list.index(t))
            disp_str = f"Task {count}: \t\t {t['title']}\n"

            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            count+=1
    option = int(input('''Enter the Task number you wish to select, 
or enter '-1' to return to menu: '''))
    #print(index)
    for i in index:
        if option == index.index(i)+1:
            print (task_list[i]['username'])
            action = int(input('''would you like to:
    1) edit or 
    2) mark work as complete?
    : '''))
            if action == 2:
                task_list[i]['completed'] = True
                print(task_list[i]['completed'])
                print('your task has been marked as completed')

            elif action == 1 and task_list[i]['completed'] == False:
                edit = int(input('''would you like to: 
    1) change the user this task was assigned to or 
    2) change its due date?
    : '''))
                if edit == 1:
                    for x in task_list:
                        print(x['username'])
                    user_change = input('write a user from those list of users above to change the task to: ')
                    task_list[i]['username'] = user_change
                    print(task_list[i]['username'])
                    print(f'the user has been updated to {user_change}')

                elif edit == 2:
                    print('the due date is: ')
                    print(task_list[i]['due_date'])
                    while True:
                        try:
                            task_due_date = input("New due date of task (YYYY-MM-DD): ")
                            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                            break

                        except ValueError:
                            print("Invalid datetime format. Please use the format specified")

                    task_list[i]['due_date'] = due_date_time
                    print(task_list[i]['due_date'])
                    print(f'your due date has been changed to {due_date_time}')
            
            elif option == -1:
                pass

def generate_report():
    print('generating your report now...\n')

    if not os.path.exists("task_overview.txt"):
        with open("Classes/21/task_overview.txt", "w") as f:
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

    with open("Classes/21/user_overview.txt", "w") as f:
        number_of_users = 0
        users = []

        for i in task_list:
            if i['username'] not in users:
                number_of_users += 1
                users.append(i['username'])
        

        for x in users:
            count = 0
            completed = 0
            uncompleted = 0
            overdue = 0
            for t in task_list:
                if t['username'] == x:
                    count +=1
                    if t['completed'] == True:
                        completed +=1
                    else:
                        uncompleted += 1
                                
            
            percentage_total = count/number_of_tasks *100
            percentage_completed = completed/count * 100
            percentage_uncompleted = uncompleted / count * 100
            f.write(f'''USER {x}:
TOTAL TASKS:    |PERCENTAGE OF ALL TASKS ASSIGNED TO THE USER:   |PERCENTAGE OF COMPLETED TASKS:  |PERCENTAGE OF UNCOMPLETED TASKS:
{count}                 {percentage_total}%                                \t {percentage_completed}%    \t\t\t\t{percentage_uncompleted}% \n''')
