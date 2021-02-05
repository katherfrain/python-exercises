color_thesaurus = {"green": "emerald", "red": "crimson",
                   "black": "obsidian", "white": "alabaster", "purple": "aubergine"}

if "emerald" in color_thesaurus.values():
    print("Emerald is in the thesaurus")
if "green" in color_thesaurus:
    print(color_thesaurus['green'])

my_name_dictionary = {"Kate": "Frain"}


def print_my_name_from_dictionary():
    for first_name_as_key in my_name_dictionary:
        print(
            f'My name is {first_name_as_key} {my_name_dictionary[first_name_as_key]}')


print_my_name_from_dictionary()


def add_my_name_to_dictionary_then_print():

    first_name_input = input('What is your first name? ')
    last_name_input = input('What is your last name? ')

    name_dictionary = {first_name_input: last_name_input}

    for all_first_names in name_dictionary:
        print(
            f'The name entered was {all_first_names} {name_dictionary[all_first_names]}')


add_my_name_to_dictionary_then_print()


home_address = {
    'street': "I don't know they keep moving", 'city': 'Charleston'}
work_address = {'street': "The online information highway",
                'city': 'World Wide Web'}

all_addresses = [home_address, work_address]

my_info_dictionary = {'firstname': 'Kate',
                      'lastname': 'Frain', 'addresses': all_addresses}
print(my_info_dictionary)


def edit_todo_list():

    todos = {}
    editing_function = input(
        '***************************************\n'
        'Press 1 to add a task\nPress 2 to delete a task\nPress 3 to view all tasks\nPress q to quit.'
        '\n*************************************\n')

    while editing_function != 'q':

        if editing_function == '1':
            task_name = input('Please enter the task to be accomplished: ')
            task_priority = input('Please enter the priority level of the task: ')

            todos[task_name] = task_priority
            
            editing_function = input(
                '***************************************\n'
                'Press 1 to add a task\nPress 2 to delete a task\nPress 3 to view all tasks\nPress q to quit.'
                '\n*************************************\n')


        elif editing_function == '2':
            task_name = input('Please enter the task name: ')
            try:
                del todos[task_name]

                editing_function = input(
                    '***************************************\n'
                    'Press 1 to add a task\nPress 2 to delete a task\nPress 3 to view all tasks\nPress q to quit.'
                    '\n*************************************\n')
            except KeyError:
                editing_function = input('That is not a task currently on the list. To print the list, press 3.')
       
        elif editing_function == '3':
            for every_value in todos:
                #when it hits this statement, look back at all the tasks, then find what they're keeping as the 'definition' of their keys and print them
                #so if the task 'key' is 'wash the dog', then it finds the priority for 'wash the dog' - which is 'high'
                #when the task 'key' isn't wash the dog, it doesn't find wash the dog's priority
                print(f'The task {every_value} is priority {todos[every_value]}')
        
            editing_function = input(
            '***************************************\n'
            'Press 1 to add a task\nPress 2 to delete a task\nPress 3 to view all tasks\nPress q to quit.'
            '\n*************************************\n')

        elif editing_function == 'q':
            break
       
        else:
                editing_function = input(
                '***************************************\n'
                'Press 1 to add a task\nPress 2 to delete a task\nPress 3 to view all tasks\nPress q to quit.'
                '\n*************************************\n')


edit_todo_list()