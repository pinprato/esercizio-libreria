#funzioni per libri
def add_book(library,lend_books,book):
        if book in library:
                print(f"Libro '{book}' è già nella libreria")
        elif book in lend_books:
                print(f"Libro '{book}' è già preso in prestito da qualcuno")
        else:
                library.append(book)
                print(f"Libro '{book}' aggiunto alla libreria")

def lend_book(library,lend_books,book):
    if book in library:
        library.remove(book)
        lend_books.append(book)
        print(f"Libro '{book}' è stato dato in prestito")
    else:
        print(f"Libro '{book}' non è disponibile nella libreria")

def return_book(library,lend_books,book):
        if book in lend_books:
                lend_books.remove(book)
                library.append(book)
                print(f"Libro '{book}' è stato restituito alla libreria")
        else:
             print(f"Libro '{book}' non è stato preso in prestito da nessuno")


def check_availability(library,book):
    if book in library:
        print(f"Libro '{book}' è disponibile nella libreria")
    else:
        print(f"Libro '{book}' non è disponibile nella libreria")

def view_books(library):
        for book in library:
                print(book, end=' ')

def view_lent_books(lent_books):
        for book in lent_books:
                print(book, end=' ')