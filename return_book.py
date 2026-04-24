from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issue_books:
        issue_books.remove(book_name)
        if book_name in books:
            books[book_name] += 1
        else:
            books[book_name] = 1
        print("Book returned successfully")
    else:
        print("This book was not issued")
