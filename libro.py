# Funzione aggiungi libro: 
# controlla se il libro è già nella libreria, se è stato preso in prestito
def add_book(library,lend_books,book):
        if book in library:
                print(f"\nLibro '{book}' è già nella libreria\n")
        elif book in lend_books:
                print(f"\nLibro '{book}' è già preso in prestito da qualcuno\n")
        else:
                library.append(book)
                print(f"\nLibro '{book}' aggiunto alla libreria\n")

# Funzione presta libro: 
# controlla se il libro è nella libreria per poterlo prestare
def lend_book(library,lend_books,book):
    if book in library:
        library.remove(book)
        lend_books.append(book)
        print(f"\nLibro '{book}' è stato dato in prestito\n")
    else:
        print(f"\nLibro '{book}' non è disponibile nella libreria\n")

# Funzione restituisci libro: 
# controlla se il libro è stato preso in prestito da qualcuno
def return_book(library,lend_books,book):
        if book in lend_books:
                lend_books.remove(book)
                library.append(book)
                print(f"\nLibro '{book}' è stato restituito alla libreria\n")
        else:
             print(f"\nLibro '{book}' non è stato preso in prestito da nessuno\n")

# Funzione visualizza disponibilità libro:
# controlla se un singolo libro è disponibile nella libreria oppure no
def check_availability(library,book):
    if book in library:
        print(f"\nLibro '{book}' è disponibile nella libreria\n")
    else:
        print(f"\nLibro '{book}' non è disponibile nella libreria\n")

# Funzione visualizza libri:
# Visualizza la lista dei libri disponibili nella libreria
def view_books(library):
        for book in library:
                print(book, end='\n')

# Funzione visualizza libri in prestito:
# Visualizza la lista dei libri dati in prestito
def view_lent_books(lent_books):
        for book in lent_books:
                print(book, end='\n')