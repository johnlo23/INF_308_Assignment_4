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
            print({borrowed[i]})
        except IndexError:
            print()


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

# Print library
print_library(book_list, available_list, borrowed_list)
