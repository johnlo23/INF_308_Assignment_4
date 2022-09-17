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


# Get the maximum of the length of two lists
def get_max_list_len(list1, list2):
    return max(len(list1), len(list2))


# Print Library to screen
def print_library(available, borrowed):
    # print Available and Borrowed lists side-by-side
    print()
    print('Available books' + ' ' * 20 + 'Borrowed books')
    print('---------------' + ' ' * 20 + '--------------')

    # Get the list length of the longest list to use in the print loop
    num_books = get_max_list_len(available, borrowed)

    # Loop through available book list
    for i in range(0, num_books):
        # Two lists may not have the same number of books, so where not matched
        # in one list, print blank space as filler
        if i in range(0, len(available)):
            print(f'{i + 1}. ', end='')
            print(f'{available[i]}' + ' ' * ((2 - len(str(i + 1))) + 30 - len(available[i])), end='')
        else:
            # Just add spaces for formatting if no entry on this line
            print(' ' * ((2 - len(str(i + 1))) + 33), end='')

        # Two lists may not have the same number of books, so skip printing
        # index number if available book is blank
        if i in range(0, len(borrowed)):
            # Print book number (Index + 1)
            print(f' {i + 1}. ', end='')
            print(f'{borrowed[i]}')
        else:
            print()


# Print action menu
def print_menu():
    print('Choose an action:')
    print('- - - - - - - - - -')
    print('(B) Borrow a book')
    print('(R) Return a book')
    print('(A) Add (donate) a Book')
    print('(S) Start over')
    print('(Q) Quit')


# Convert string to an Integer
def to_int(string):
    try:
        # Attempt convert to float first in case user used a decimal point
        float_val = float(string)
        int_val = int(float_val)
    except ValueError:
        int_val = 0

    return int_val


# Get user action choice
def get_user_choice():
    user_input = input('Type the letter of your choice and hit <enter>: ')
    # Convert all letter to Upper Case to make if statements simpler
    user_input = user_input.upper()

    return user_input


# Chose a random book from the list
def get_random_book(from_list):
    # Upper limit of random range will be length of the list
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


# Add a book to the borrow list
def add_book(to_list):
    print()
    print('Thank you for donating!')
    # Continue loop until user enters a book name
    while True:
        book_name = input('What is the title of this book? ')
        # Verify user typed at least one character
        if len(book_name) > 0:
            to_list.append(book_name)
            break
        else:
            print('Please type in the title of your book.')
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

# Print library and menu until user quits
while True:
    # Print library
    print_library(available_list, borrowed_list)
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
        elif user_choice == 'A':
            add_book(available_list)
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
