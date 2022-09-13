# CINF-308 Fall 2022
# Assignment 4
# John Logiudice


# Welcome message
welcome_message = 'The Classic Fiction Lending Library\n' \
    + '- ' * 20 + '\n' \
    + 'Welcome to our library\n' \
    + '\n'
print(welcome_message)

# Get list of books from text file
file = open('books.txt', 'r')
book_list = [readline.rstrip() for readline in file]
file.close()

# Create a copy of book_list into available_list
available_list = book_list.copy()

# Create empty list of borrowed books
borrowed_list = list()

# print Available and Borrowed lists side-by-side
print("Available books" + " "*22 + "Borrowed books")
print("---------------" + " "*22  + "--------------")

for i in range(0, len(available_list)):
    print(f"{i+1}. {available_list[i]}" + " "*((2-len(str(i+1)))+30-len(available_list[i])), end="")
    print(f"{i + 1}. ", end="")
    try:
        print({borrowed_list[i]})
    except IndexError:
        print()
