# CINF-308 Fall 2022
# Assignment 4
# John Logiudice


# Get list of items from text file
def get_list_from_file(file_name):
    file = open(file_name, 'r')
    name_list = [readline.rstrip() for readline in file]
    file.close()
    name_list.sort()
    return name_list


# Print Library
def print_library(books, available, borrowed):
    # print Available and Borrowed lists side-by-side
    print("Available books" + " " * 20 + "Borrowed books")
    print("---------------" + " " * 20 + "--------------")

    for i in range(0, len(books)):
        print(f"{i+1}. ", end="")
        # Available list may not have same number of items as book list
        # so use try to handle index errors
        try:
            print(f"{available[i]}" + " "*((2-len(str(i+1)))+30-len(available[i])), end="")
        except IndexError:
            print(" "*((2-len(str(i+1)))+30), end="")

        print(f"{i + 1}. ", end="")
        # Borrowed list may not have same number of items as book list
        # so use try to handle index errors
        try:
            print(f"{borrowed[i]}")
        except IndexError:
            print()


# Print action menu
def print_menu():
    print('Choose an action:')
    print('- - - - - - - - - -')
    print('(B) Borrow a book')
    print('(R) Return a book')
    print('(S) Start over')
    print('(Q) Quit')


# Get user action choice
def get_user_choice():
    user_input = input('Type the letter of your choice and hit enter: ')
    user_input = user_input.upper()
    return user_input

# Get book number
def get_book_number(action):
    if action == 'B':
        action_type = 'borrow'
    else:
        action_type = 'return'
    action_choice = input(f'Enter the number of the book to {action_type} and hit enter: ')
    # Add error check
    try:
        action_choice = int(action_choice)
    except ValueError:
        print()
    return action_choice


# Borrow a book
def move_book(from_list, to_list):
    book_number = get_book_number('B')
    try:
        to_list.append(from_list.pop(book_number - 1))
    except IndexError:
        print()
    to_list.sort()



# Welcome message
welcome_message = 'The Classic Fiction Lending Library\n' \
    + '- ' * 20 + '\n' \
    + 'Welcome to our library\n' \
    + '\n'
print(welcome_message)

# Get list of books from text file
book_list = get_list_from_file("books.txt")

# Create a copy of book_list into available_list
available_list = book_list.copy()

# Create empty list of borrowed books
borrowed_list = list()

# Print library and message until user quits
while True:
    # Print library
    print_library(book_list, available_list, borrowed_list)
    print()

    # Print action menu
    print_menu()

    user_choice = get_user_choice()
    if user_choice == 'B':
        move_book(available_list, borrowed_list)
    elif user_choice == 'R':
        move_book(borrowed_list, available_list)
    elif user_choice == 'S':
        available_list = book_list.copy()
        borrowed_list.clear()
    elif user_choice == 'Q':
        break

    print()

print("Goodbye!")