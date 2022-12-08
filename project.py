import json
from colored import fg, bg, attr
import os
import os.path
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import random

# webhookUrl = "https://discord.com/api/webhooks/1050531048779415673/7_HRW7evaDHSuIs8Nd90xDnEHreUu2VT4nS4jqDKagAvsVk-l6xhiqgzPm2m-AFMexNP"
# webhook = DiscordWebhook(url=webhookUrl)
# colours = [
#         '765bd9',
#         'e31053',
#         '6a00ff',
#         '0092fa',
#         '5df06f',
#         'f08800'
#     ]
# randomPicker = random.choice(colours)

# Colours
white = fg(15)
purple = fg(57)
blue = fg(27)
green = fg(10)
red = fg(160)
orange = fg(202)
pink = fg(198)


# Load the JSON file
with open('list_config.json') as f:
    config = json.load(f)

# Get the default file name from the config
defaultFile = config.get('defaultFile')

# Load the default file
with open(f"{defaultFile}.json") as f:
    todos = json.load(f)

def print_todos():
    with open(f"{defaultFile}.json") as f:
        _todos = json.load(f)

        for todo in _todos:
# Print the identifier and name of the todo
            status = ''

            # Check the status of the todo
            if todo['status'] == 1:
                status = f"{green}Finished"
                # If it's finished, print the todo in green
                print(f"{green}{todo['id']} - {todo['name']} [{status}]{white}")
            elif todo['status'] == 2:
                status = f"{orange}Started"
                # If it's started, print the todo in orange
                print(f"{orange}{todo['id']} - {todo['name']} [{status}]{white}")
            else:
                status = f"{red}Unfinished"
                # If it's not started or finished, print the todo in red
                print(f"{red}{todo['id']} - {todo['name']} [{status}]{white}")

def add_todo(todo_name):
    # Load the todos from the JSON file
    with open(f"{defaultFile}.json") as f:
        todos = json.load(f)

    # Set the initial status of the todo to unfinished
    todo_status = 0

    # Get the ID of the last todo in the list, or 1 if the list is empty
    if todos:
        last_id = todos[-1]['id']
    else:
        last_id = 0

    # Create a new todo with the specified name and status, and the next ID in the sequence
    new_todo = {'id': last_id + 1, 'name': todo_name, 'status': todo_status}

    # Add the new todo to the list of todos
    todos.append(new_todo)
    
    # embed = DiscordEmbed(title='New Todo Added', description=f'ID: {new_todo["id"]}\nName: {new_todo["name"]}', color=f"{randomPicker}")

    # # Set the webhook's content and send it
    # webhook.content = 'New todo added to the list'
    # webhook.add_embed(embed)
    # webhook.execute()


    # Save the updated list of todos to the JSON file
    with open(f"{defaultFile}.json", 'w') as f:
        json.dump(todos, f)


def update_todo(todo_id, new_status):
    with open(f"{defaultFile}.json") as f:
        todos = json.load(f)
# Loop through the list of todos
    for todo in todos:
        # Check if the current todo has the specified ID
        if todo['id'] == todo_id:
        # If it does, update its status
            todo['status'] = new_status

        # Stop looping through the list
            break
    
    with open(f"{defaultFile}.json", 'w') as f:
        json.dump(todos, f)

    # Save the updated list of todos to the JSON file
def edit_todo(todo_id, new_name):
  # Load the JSON file
    with open(f"{defaultFile}.json") as f:
        todos = json.load(f)

  # Loop through the list of todos
    for todo in todos:
    # Check if the current todo has the specified ID
        if todo['id'] == todo_id:
      # If it does, update its name
            todo['name'] = new_name

      # Stop looping through the list
            break

  # Save the updated list of todos to the JSON file
    with open(f"{defaultFile}.json", 'w') as f:
        json.dump(todos, f)


def remove_todo(todo_id):
    with open(f"{defaultFile}.json") as f:
        todos = json.load(f)

    for todo in todos:
        # Check if the current todo has the specified ID
        if todo['id'] == todo_id:
        # If it does, remove it from the list
            todos.remove(todo)

        # Stop looping through the list
        break

    # Loop through the list of todos again
    for todo in todos:
        # Check if the current todo has an ID greater than the ID of the todo you want to remove
        if todo['id'] > todo_id:
        # If it does, decrease its ID by 1
            todo['id'] -= 1

    # Save the updated list of todos to the JSON file
    with open(f"{defaultFile}.json", 'w') as f:
        json.dump(todos, f)

def set_new_defaultFile(defaultFile):
    newFile = {"defaultFile":f"{defaultFile}"}
    with open("list_config.json", 'w') as f:
        json.dump(newFile, f)

    if not os.path.exists(f"{defaultFile}.json"):
        data = []
        with open(f"{defaultFile}.json", 'w'):
            json.dump(data, f)

def clearFile():
    with open(f"{defaultFile}.json") as f:
        todos = json.load(f)
    data = []

    with open(f"{defaultFile}.json", 'w') as f:
        json.dump(data, f)

def import_todos(file_name):
    with open(f"{file_name}.txt", 'r') as f:
        file_contents = f.read()

    # Split the file contents on newlines
    todos = file_contents.split('\n')

    # Create a list of todos with the specified format
    todos_list = [{'id': i, 'name': todo, 'status': 0} for i, todo in enumerate(todos)]

    # Save the todos to the JSON file
    with open(f"{defaultFile}.json", 'w') as f:
        json.dump(todos_list, f)

# Keep prompting the user to delete todos until they enter "done"

# # Print the list of todos
# print_todos()

# # Add a new todo
# add_todo()

# # Update an existing todo
# update_todo()

def cls():
    os.system('cls')

def menu():
    print(
f'''{white}Current File - {purple}{defaultFile}.json

{pink}[{white}1{pink}] {white}List Todo's
{pink}[{white}2{pink}] {white}Add New Todo
{pink}[{white}3{pink}] {white}Update Todo Status
{pink}[{white}4{pink}] {white}Remove Todo's
{pink}[{white}5{pink}] {white}Edit Todo's Name
{pink}[{white}6{pink}] {white}Set new default File [Also creates the file when set.]
{pink}[{white}7{pink}] {white}Clear all todo's
{pink}[{white}8{pink}] {white}Import todo's from file [Available formats - TXT (More will come later)]{white}

''')

while True:
    menu()
    inputFunc = int(input(f'{pink}>{white} '))
    
    if inputFunc == 1:
        cls()
        print_todos()
        input(f'\nType "{purple}done{white}" whenever ready. - ')
        cls()
    elif inputFunc == 2:
        cls()
        while True:
            print_todos()
            # Prompt the user to add a todo
            response = input(f'\nEnter the name of the todo to add, or "{purple}done{white}" to exit: ')

            # Check if the user entered "done"
            if response == 'done':
                # If they did, exit the loop
                break

            # Otherwise, add the todo
            add_todo(response)
            cls()

    elif inputFunc == 3:
        while True:
            print_todos()

            # Prompt the user for the ID of the todo they want to edit
            todo1 = input(f'\nEnter the ID of the todo to edit, or "{purple}done{white}" to exit: ')

            # Check if the user entered "done"
            if todo1 == 'done':
                # If they did, exit the loop
                break

            # Try to convert the user's input to an integer
            try:
                todo_id = int(todo1)
            except ValueError:
                # If the user's input cannot be converted to an integer, print an error message
                print(f'Invalid input. Please enter a valid todo ID or "{purple}done{white}" to exit.')
                continue

            # Prompt the user for the new status of the todo
            new_status = int(input(f'Enter the new status of the todo (0 for {red}unfinished{white}, 1 for {green}finished{white}, or 2 for {orange}started{white}): '))

            # Update the todo with the specified ID
            update_todo(todo_id,new_status)
            cls()
    elif inputFunc == 4:
        cls()
        while True:
    # Print the list of todos
            # Print the list of todos
            print_todos()

            # Prompt the user to delete a todo
            response = input(f'\nEnter the ID of the todo to remove, or "{purple}done{white}" to exit: ')

            # Check if the user entered "done"
            if response == 'done':
                # If they did, exit the loop
                break

            # Otherwise, try to convert the user's input to an integer
            try:
                todo_id = int(response)
            except ValueError:
                # If the user's input cannot be converted to an integer, print an error message
                print(f'Invalid input. Please enter a valid todo ID or "{purple}done{white}" to exit.')
                continue

            # If the user's input was successfully converted to an integer, delete the todo
            remove_todo(todo_id)
            cls()
    elif inputFunc == 5:
        while True:
            print_todos()

            response = input(f'\nEnter the ID of the todo to edit, or "{purple}done{white}" to exit: ')

            if response == 'done':
                break

            try:
                todo_id = int(response)
            except ValueError:
                print(f'Invalid input. Please enter a valid todo ID or "{purple}done{white}" to exit.')

            new_edit = input('What would you like to change the current name to?: ')

            edit_todo(todo_id, new_edit)

    elif inputFunc == 6:
        cls()
        defaultFile = input(f'What is the new file called, does not need to include the "{pink}.json{white}" extension. [example: {pink}newFile{white}]: ')
        set_new_defaultFile(defaultFile)
        # print('When setting a new file, the program requires a restart due to the new default file not updating. Press enter to exit the program.')
        # input()
        # exit()
    elif inputFunc == 7:
        cls()
        clearFile()
        print(f'{pink}>{white} Cleared Current File')
    elif inputFunc == 8:
        cls()
        fileName = input(f"{pink}>{white} What is the file name? extension not required. {pink}- ")
        import_todos(fileName)
