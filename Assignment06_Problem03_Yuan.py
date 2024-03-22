#Assignment 06 - Problem Libarary Management System

# Create a class hierarchy for a Library Management System. The base class should be an abstract class
# called LibraryItem, which represents items that can be borrowed from the library. The LibraryItem class
# should define the following:
# • An initializer (__init__) that includes properties such as title, subject, and location in the library.
# • Abstract methods check_out() and return_item() that must be implemented by subclasses to
# handle the borrowing and returning of items.
# • A method get_details() that prints the details of the item.
# Derive the following classes from LibraryItem:
# Book, which has additional properties like author and ISBN. It should override the abstract methods to
# update the status of the book when it is checked out or returned.
# DVD, which has additional properties such as director, genre, and run_time. It should override the
# abstract methods with its own logic for checking out and returning.
# Journal, with additional properties like volume and issue_number, again overriding the abstract
# methods.
# Create a LibraryCatalog class that maintains a list of LibraryItems. It should have the following methods:
# • add_item(), which adds a new LibraryItem to the catalog.
# • remove_item(), which removes an item from the catalog.
# • find_item_by_title(), which searches for an item by title and returns it.
# • check_out_item(), which checks out an item by calling its check_out() method.
# • return_item(), which returns an item by calling its return_item() method.


class LibraryItem:
    def __init__(self, title, subject, location):
        self.title = title
        self.subject = subject
        self.location = location
        self.checked_out = False

    def check_out():
        pass

    def return_item():
        pass

    def get_details(self):
        print("Title: " + str(self.title) + "\n")
        print("Subject: " + str(self.subject) + "\n")
        print("Location: " + str(self.location) + "\n")
        if self.checked_out:
            print("Status: Checked out.\n")
        else:
            print("Status: Returned.\n")


class Book(LibraryItem):
    def __init__(self, title, subject, location, author, ISBN):
        super().__init__(title, subject, location)
        self.author = author
        self.ISBN = ISBN

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print("Check out success.\n")
        else:
            print("Could not check out.\n")


    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print("Return success.\n")
        else:
            print("Could not return.\n")

    def get_details(self):
        super().get_details()
        print("Author: " + str(self.author) + "\n")
        print("ISBN: " + str(self.ISBN) + "\n")

class DVD(LibraryItem):
    def __init__(self, title, subject, location, director, genre, run_time):
        super().__init__(title, subject, location)
        self.director = director
        self.genre = genre
        self.run_time = run_time
    
    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print("Check out success.\n")
        else:
            print("Could not check out.\n")


    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print("Return success.\n")
        else:
            print("Could not return.\n")

    def get_details(self):
        super().get_details()
        print("Director: " + str(self.director) + "\n")
        print("Genre: " + str(self.genre) + "\n")
        print("Run Time: " + str(self.run_time) + "min.\n")

class Journal(LibraryItem):
    def __init__(self, title, subject, location, volume, issue_number):
        super().__init__(title, subject, location)
        self.volume = volume
        self.issue_number = issue_number

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print("Check out success.\n")
        else:
            print("Could not check out.\n")


    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print("Return success.\n")
        else:
            print("Could not return.\n")

    def get_details(self):
        super().get_details()
        print("Volume: " + str(self.volume) + "\n")
        print("Issue Number: " + str(self.issue_number) + "\n")


class LibraryCatalog():
    def __init__(self):
        self.catalog = []

    def add_item(self, target_item):
        if target_item not in self.catalog:
            self.catalog.append(target_item)
            print("Item appended.\n")
        else:
            print("Item exists in the catalog.\n")
    
    def remove_item(self, target_item):
        if target_item in self.catalog:
            self.catalog.remove(target_item)
            print("Item removed.\n")
        else:
            print("Could not find item in the catalog.\n")
    
    def find_item_by_title(self, title):
        for item in self.catalog:
            if item.title == title:
                return item  # Return the found item
        print("Could not find item with this title.\n")
            
    def check_out_item(self, target_item):
        if target_item in self.catalog:
            target_item.check_out()
            print("Item checked out.\n")
        else:
            print("Failed.\n")
        
    def return_in_item(self, target_item):
        if target_item in self.catalog:
            target_item.return_item()
            print("Item returned.\n")
        else:
            print("Failed.\n")


#=============================================================
def main():
    Catalog = LibraryCatalog()

    book1 = Book("Zeus", "Myth", "F1", "Unknown", 2233)
    Catalog.add_item(book1)

    DVD1 = DVD("Fire", "Science", "F2", "Who", "Science", 120)
    Catalog.add_item(DVD1)
    DVD1.get_details()

    Catalog.find_item_by_title("Zeus")
    Catalog.check_out_item(book1)
    Catalog.return_in_item(book1)
    Catalog.remove_item(book1)

#==============================================================
main()