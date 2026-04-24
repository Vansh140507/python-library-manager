from utils import books, issue_books

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books and books[book_name] > 0:
        books[book_name] -= 1
        if books[book_name] == 0:
            del books[book_name]
        issue_books.append(book_name)
        print("Book issued successfully")
    else:
        print("Book not available")
