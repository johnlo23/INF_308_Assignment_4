# CINF-308 Fall 2022
# Assignment 4
# John Logiudice

import random

# Get list of items from text file
def get_list_from_file(file_name):
    # File is one book per line
    file = open(file_name, 'r')
    # Read each line from file. Remove trailing newline char
    name_list = [readline.rstrip() for readline in file]
    file.close()
    name_list.sort()

    return name_list


# Print Library to screen
def print_library(available, borrowed, num_books):
    # print Available and Borrowed lists side-by-side
    print()
    print('Available books' + ' ' * 19 + 'Borrowed books')
    print('---------------' + ' ' * 19 + '--------------')

    # Loop through available book list
    for i in range(0, num_books):
        # Print book number (Index + 1)
        print(f'{i+1}. ', end='')
        # Available list may not have same number of items as num_books
        # so use try to handle index errors
        try:
            print(f'{available[i]}' + ' '*((2-len(str(i+1)))+30-len(available[i])), end='')
        except IndexError:
            print(' '*((2-len(str(i+1)))+30), end='')

        print(f'{i + 1}. ', end='')
        # Borrowed list may not have same number of items as num_books
        # so use try to handle index errors
        try:
            print(f'{borrowed[i]}')
        except IndexError:
            print()


# Print action menu
def print_menu():
    print('Choose an action:')
    print('- - - - - - - - - -')
    print('(B) Borrow a book')
    print('(R) Return a book')
    print('(S) Start over (Return All)')
    print('(Q) Quit')


# Convert string to an Integer
def to_int(string):
    try:
        float_val = float(string)
        int_val = int(float_val)
    except ValueError:
        int_val = 0

    return int_val


# Get user action choice
def get_user_choice():
    user_input = input('Type the letter of your choice and hit <enter>: ')
    user_input = user_input.upper()

    return user_input


# Chose a random book from the list
def get_random_book(from_list):
    list_len = len(from_list)
    if list_len > 0:
        return random.randrange(0, list_len)
    else:
        return -1


# Convert action type to a user-friendly string
def action_type(action):
    if action == 'B':
        return 'borrow'
    else:
        return 'return'


# Get book number
def get_book_number(action):
    while True:
        # Ask user for book number
        action_choice = input(f"Type the number of the book to {action_type(action)} " 
                              "or 'R' for random, then hit <enter> (blank or 0 to exit): ")
        # Use try to handle invalid (non-integer) input from user
        if action_choice.upper() == 'R':
            action_choice = -1
            break
        else:
            try:
                action_choice = to_int(action_choice)
                break
            except ValueError:
                print(f'Please type a book number currently on the {action_type(action)} list.')

    return action_choice


# Move a book from one list to the other
def move_book(from_list, to_list, action):
    while True:
        # Ask user for a book number. Subtract 1 to align with list.
        book_number = get_book_number(action) - 1

        # Chose book at random
        if book_number == -2:
            book_number = get_random_book(from_list)

        # User did not enter a valid number
        if book_number == -1:
            break
        # User did not choose a number of a book on the from list
        elif book_number not in range(0, len(from_list)):
            print('That book number is not valid.')
        # Move book from from_list to to_list
        else:
            to_list.append(from_list.pop(book_number))
            break
    to_list.sort()


# Welcome message
welcome_message = 'The Classic Fiction Lending Library\n' \
    '- - - - - - - - - - - - - - - - - - \n' \
    'Welcome to our library.\n' \
    'You can borrow these books for free. Please return them promptly when you are done.\n'
print(welcome_message)

# Get list of books from text file
book_list = get_list_from_file('books.txt')

# Create a copy of book_list into available_list
available_list = book_list.copy()

# Create empty list of borrowed books
borrowed_list = list()

# Print library and message until user quits
while True:
    # Print library
    print_library(available_list, borrowed_list, len(book_list))
    print()

    # Print action menu
    print_menu()

    # Ask user to choose an action
    while True:
        user_choice = get_user_choice()
        if user_choice == 'B':
            # If list is empty
            if len(available_list) == 0:
                print('There are no books available to borrow.')
            else:
                move_book(available_list, borrowed_list, user_choice)
                break
        elif user_choice == 'R':
            # If list is empty
            if len(borrowed_list) == 0:
                print('There are no books available to return.')
            else:
                move_book(borrowed_list, available_list, user_choice)
                break
        elif user_choice == 'S':
            available_list = book_list.copy()
            borrowed_list.clear()
            break
        elif user_choice == 'Q':
            print()
            print('Goodbye!')
            quit(0)
        else:
            print('That is not a valid action.')
