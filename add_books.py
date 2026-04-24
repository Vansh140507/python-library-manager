from utils import books

def add():
    book_name = input("Enter the Book name to add: ").upper()
    copies = int(input("Enter number of copies to add: "))
    if book_name in books:
        books[book_name] += copies
    else:
        books[book_name] = copies
    print(f"Book Added: {book_name} | Total Copies: {books[book_name]}")
