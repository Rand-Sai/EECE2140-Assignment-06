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
