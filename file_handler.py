import csv

def load_books():
    books = {}

    try:
        with open("library_dataset_updated.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books[row["Title"]] = {

                    "Author": row["Author"],
                    "Price": int(row["Price"]),
                    "Availability": row["Availability"] == "True"
                

                }
    except FileNotFoundError:
        print("File not found , creating new one.")
    return books

def save_books(books):
    with open("ibrary_dataset_updated.csv", "w", newline='') as file:
        fieldnames = ["title","author", "price","availability"]
        writer = csv.DictWriter(file , fieldnames=fieldnames)

        writer.writeheader()
        for title, details in books.items():
            writer.writerow({
                "title": title,
                "author": details["Author"],
                "price": details["Price"],
                "availability": details["Availability"]

            })