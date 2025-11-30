import book_library

# Create object book_manager
book_manager = book_library.BookManager()

while True:
    # Display menu
    user_choice = input("Please select option:\n1 - Add new book\n2 - View all books\n3 - Search for the book using the title\n")

    if user_choice == '1':
        # Validate input
        try:
            book_title  = input("Enter the title of the book\n")
            book_author = input("Enter the author's name\n")
            book_year   = input("Enter the release date\n")

            book = book_library.Book(book_title, book_author, book_year)
            book_manager.add_book(book)
            print("New book has been added to the library")
        except:
            print("Incorrect information")

    # Print full library       
    elif user_choice == '2':
        print("Full library")
        book_manager.show_library()
        print("-" * 20)
    
    # Look up book by the title
    elif user_choice == '3':
        title = input("Please input the title of the book\n")
        book_manager.look_up_book(title)

