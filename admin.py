from file_handler import save_books

def add_book(books):
    title = input("Enter title: ")
    Author = input("Enter author: ")
    try:
        Price = int(input("Enter price: "))
    except ValueError:
        print("Invalid price")
        return
    
    books[title] = {

        "Author": Author,
        "Price": Price,
        "Availability": True

    }
    save_books(books)
    print("Book added successfully!")

def update_book(books):
    title = input("Enter book title to update: ")
    if title in books:
        try:
            Price = int(input("Enter new price: "))
            books[title]["Price"] = Price
            save_books(books)
            print("Book updated successfuly!")
        except ValueError:
            print("Invalid price")
    else:
        print("Book not found!")
def delete_book(books):
    title =  input("Enter book title to delete: ")
    if title in books:
        del books[title]
        save_books(books)
        print("Book deleted successfully!")
    else:
        print("Book not found!")
def admin_menu(books):
    while True:
        print("\n -- Admin Menu ---")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            update_book(books)
        elif choice == "3":
            delete_book(books)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            

    
    