global library
library = {
    'Journey to the Center of the Earth': 'Jules Verne',
    'Twenty Thousand Leagues Under the Seas': 'Jules Verne',
    'Project Hail Mary': 'Andy Weir',
    'The Martian': 'Andy Weir',
    'Ready Player One': 'Ernest Cline',
    }

def add_book(name, author):
    library[name] = author

def find_by_name(name):
    return name, library[name]

def find_by_author(author):
    res = []
    for book in library:
        if library[book] == author:
            res.append(book)
    if not res:
        print("No book found")
        return
    return res, author

def print_library():
    for book in library:
        print(f"{book} {' ' * (40 - len(book))} {library[book]}")

add_book("The Invisible Man", "H. G. Wells")
print(find_by_author("Andy Weir"))
print(find_by_name("The Martian"))
print_library()