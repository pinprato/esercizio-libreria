"""
Gestionale semplice libreria

Aggiunta libro
Prestito libro
Ritornare libro
Disponibilità libro
Libri disponibili nella libreria
Libri dati in prestito
"""
# Importazione del file libro.py per le funzioni da utilizzare
from libro import * 

#lista vuote di libreria e libri dati in prestito
library = []
lend_books = []


def main():
    
    print("Gestionale libreria")
    # Il menù viene visualizzato all'inizio del programma ed ogni volta che una scelta è stata completata,
    # finché riceve da input il numero 7
    while True:
        print("\nScegliere tra le seguenti opzioni:")
        print("1. Aggiungi libro")
        print("2. Prendi in prestito libro")
        print("3. Ritorna libro")
        print("4. Controlla disponibilità libro")
        print("5. Visualizza libri nella libreria")
        print("6. Visualizza libri dati in prestito")
        print("7. Exit")
        
        choice = input("Selezionare opzione:")
        
        if choice == '1':
            book = input("Scrivere il nome del libro da aggiungere: ")
            add_book(library,lend_books,book)
        
        elif choice == '2':
            book = input("Scrivere il nome del libro da dare in prestito: ")
            lend_book(library,lend_books,book)
        
        elif choice == '3':
            book = input("Scrivere il nome del libro da restituire: ")
            return_book(library,lend_books,book)
        
        elif choice == '4':
            book = input("Scrivere il nome del libro da verificare la disponibilità: ")
            check_availability(library,book)
        
        elif choice == '5':
            view_books(library)

        elif choice == '6':
            view_lent_books(lend_books)

        elif choice == '7':
            print("Arrivederci!")
            break
        
        else:
            print("Opzione non valida. Riprovare.")

if __name__ == "__main__":
    main()
