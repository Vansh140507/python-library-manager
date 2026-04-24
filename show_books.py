from utils import books

def show():
    if len(books) == 0:
        print("No books available")
    else:
        print(f"\n{'Book Name':}     {'Copies Available'}")
        print("-" * 45)
        for name, copies in books.items():
            print(f"{name:}      {copies}")
