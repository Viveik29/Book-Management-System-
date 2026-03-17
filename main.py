from file_handler import load_books
from admin import admin_menu
from user import user_menu

def main():
    books = load_books()

    while True:
        print("\n===== Book Management System =====")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_menu(books)
        elif choice == "2":
            user_menu(books)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
    