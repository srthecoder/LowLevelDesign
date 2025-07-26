# Design a Library System.

"""
Entities -

Library --> Stores Books 
User --> Borrows/Returns

"""
"""
1. are we looking at subtypes of books? E book/ physical or Genre
2. Possible operations - CRUD, Add books, remove books, search books...what is your focus?

Relationships :
Library HAS A book (aggregation)

Functionalities:

Library --> Searchbook() , addbook(), removebook()

Book --> creating book entities

User --> creating user info

Booking --> map book to user, 
borrow(), return()

"""


# search - name/location....if yes...what kind of search are we looking at? "Prefix?/ complete"


class Library():
    books = [] #stores book objects in Library
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def searchBook(book):
        if Library.books: #non-empty
            if book in Library.books: #if object present in list, print title
                print(f"{book.title} found in Library.")
                return 1
            else:
                print(f"{book.title} not found in Library.")
                return 0
        else:
            print(f"Library is empty.")
            return -1
    
    @staticmethod
    def addBook(book):
        Library.books.append(book) #add object to object list

    @staticmethod
    def removeBook(book):
        Library.books.remove(book) #remove book object from object list

    @staticmethod
    def showcase():
        for book in Library.books:
            print(f"Title: {book.title}    Author: {book.author}   Pages: {book.pages}")



class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


class User():
    def __init__(self, name, userId, emailId):
        self.name = name
        self.userId = userId
        self.emailId = emailId

from collections import defaultdict
class Booking():
    logbook = defaultdict(list)
    # {'USERID1':[b1, b2], 'USERID2':[b3]}

    def __init__(self):
        pass
    
    def borrowBook(user, book):
        if Library.searchBook(book) == 1: #book exists
            uid = user.userId
            for books in Booking.logbook.values():
                if book in books:
                    return f"\n{book.title} is unavailable."
                
            if uid not in Booking.logbook:
                Booking.logbook[uid] = book
            else:
                Booking.logbook[uid].append(book)
            return f"\n{user.name} has successfully borrowed book - {book.title}."
        else:
            return f"\nThis book is not available at this library."

    def returnBook(user, book):
        if Library.searchBook(book) == 1:
            uid = user.userId
            if uid not in Booking.logbook or not Booking.logbook[uid]:
                return f"\n{user.name} has not borrowed a book from this library."
            else:
                Booking.logbook[uid].remove(book)
                return f"\n{user.name} has successfully returned book - {book.title}."
        else:
            return f"\nThis book is not from this library."


b1 = Book("Harry Potter", "JK Rowling", 350)
b2 = Book("Sherlock", "Arthur Conan Doyle", 550)
b3 = Book("Donkeys in the sand", "Roald Dahl", 150)

lib = Library("Los Angeles Public Library", "Los Angeles")

print(f"\n Searching for Book {b1.title}:")
Library.searchBook(b1)

print(f"\n Adding Books to Library:")
Library.addBook(b1)
Library.addBook(b2)
Library.addBook(b3)
Library.showcase()
print("\n removing Book:")
Library.removeBook(b3)
Library.showcase()


print("\n Creating User Profiles:")
u1 = User("John", "USGVBJK21", "john@gmail.com")
u2 = User("Kelly", "KHDG78110", "kelly@gmail.com")

print(Booking.borrowBook(u1, b1))
print(Booking.returnBook(u2, b3))
print(Booking.borrowBook(u2, b2))
print(Booking.borrowBook(u2, b3))
print(Booking.borrowBook(u2, b3))