# Define class
class Book:  
    # Initialize methods 
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    @property
    def title(self):
        return self._title
    
    # Validation
    @title.setter
    def title(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Author name cannot be empty.")
        self._author = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if not str(value).isdigit():
            raise ValueError("Year must be a number.")
        self._year = int(value)
    
    # View detailed information of the book
    def __str__(self):
        return f"{self.title} - {self.author} - {self.year}"


class BookManager:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    # Iterate over the array of the book and print detailed information.
    def show_library(self):
        for book in self._books:
            print(book)
    
    # Iterate over the array and find the "book" object with matching "title" property
    def look_up_book(self, title):
        for book in self._books:
            if book.title == title:
                print(book)
                break
        else:
            print("Book not found")