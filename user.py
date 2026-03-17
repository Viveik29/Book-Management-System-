from file_handler import save_books

def display_books(books):
    print("\nAvailable Books:")
    for title, details in books.items():
        status = "Available" if details["Availability"] else "Not Available"
        print(f"{title} | {details['Author']} | {details['Price']} | {status}")


def borrow_book(books):
    title = input("Enter book name to borrow: ")
    if title in books:
        if books[title]["Availability"]:
            books[title]["Availability"] = False
            save_books(books)
            print("Book borrowed successfully!")
        else:
            print("Book is already borrowed!")
    else:
        print("Book not found!")


def return_book(books):
    title = input("Enter book name to return: ")
    if title in books:
        books[title]["Availability"] = True
        save_books(books)
        print("Book returned successfully!")
    else:
        print("Book not found!")


def user_menu(books):
    while True:
        print("\n--- User Menu ---")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            display_books(books)
        elif choice == "2":
            borrow_book(books)
        elif choice == "3":
            return_book(books)
        elif choice == "4":
            break
        else:
            print("Invalid choice")