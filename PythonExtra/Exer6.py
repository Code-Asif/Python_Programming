#Library Management System
import os
import sys

class library:
    def __init__(self, UNB, title, author, genre, content):  # UNB is unique book number
        self.UNB = UNB
        self.title = title
        self.author = author
        self.genre = genre
        self.content = content

    def display_details(self):
        print(f"The details of book {self.UNB} are:")
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"genre: {self.genre}")
        print(f"content: {self.content}")
        print(self.content)

    def save_to_file(self):
        filename = f"{self.UNB}.txt"
        file_path = os.path.join("book_data", filename)

        with open(file_path, "w") as file:
            file.write(f"UNB:{self.UNB}\n")
            file.write(f"title: {self.title}\n")
            file.write(f"author: {self.author}\n")
            file.write(f"genre: {self.genre}\n")
            file.write(f"content: {self.content}\n")


# Create a directory to store employee data files
os.makedirs("book_data", exist_ok=True)

# Create a list to store employee objects
books = []


def load_books():
    for filename in os.listdir("book_data"):
        if filename.endswith(".txt"):
            file_path = os.path.join("book_data", filename)
            with open(file_path, "r") as file:
                lines = file.readlines()
                emp_dict = {}
                for line in lines:
                    key_value = line.strip().split(":", 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        emp_dict[key.strip()] = value.strip()
                # print(emp_dict)

                emp = library(
                    emp_dict["UNB"],
                    emp_dict["title"],
                    emp_dict["author"],
                    emp_dict["genre"],
                    emp_dict["content"],
                )
                books.append(emp)


load_books()


# Function to add employee details
def add_book():
    UNB = input("Enter the UNB(unique book number): ")
    for emp in books:
        if emp.UNB == UNB:
            print("A book with the same UNB already exists.")
            return
    title = input("Enter the title: ")
    author = input("Enter the author name: ")
    genre = input("Enter the genre: ")

    print(
        "Enter the content:- (type '#' on a line by itself to finish):"
    )  # it is used for taking many paragraphs
    content_lines = []
    while True:
        line = sys.stdin.readline().strip()
        if line == ".":
            break
        content_lines.append(line)
    content = "\n".join(content_lines)

    for emp in books:
        if emp.UNB == UNB:
            print("A book already exists with the same UNB.")
            return

    emp = library(UNB, title, author, genre, content)
    emp.save_to_file()
    books.append(emp)
    print("Book details added successfully!")


# Function to display employee details by EMid
def display_book_details():
    UNB = input("Enter the UNB to display details: ")
    found = False
    print("\n")
    for emp in books:
        if emp.UNB == UNB:
            emp.display_details()
            found = True
            break
    print("\n")
    if not found:
        print("book not found!")
        print("\n")


def update_book_details():
    UNB = input("Enter the UNB of book to modify: ")
    # Check if the file exists
    if os.path.exists(os.path.join("book_data", UNB + ".txt")):
        # Open the file in write mode
        with open(UNB + ".txt", "w") as file:
            print("Enter the new details:")
            title = input("title: ")
            author = input("author: ")
            genre = input("genre: ")
            content = input("content: ")

            # Write the updated details to the file
            file.write(f"UNB: { UNB}\n")
            file.write(f"title: { title}\n")
            file.write(f"author: { author}\n")
            file.write(f"genre: { genre}\n")
            file.write(f"content: { content}\n")

            print("book details updated successfully.")
    else:
        print("book not found.")


def print_all_books():
    print("List of all UNB:")
    for book in books:
        print(f"{book.UNB}: {book.title}")


print_all_books()


# Main loop
print("\n")

while True:
    print("select below options for particular action:-  ")
    print("1. Add book")
    print("2. Display  book Details")
    print("3. modify  book Details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_book_details()
    elif choice == "3":
        update_book_details()

    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
        print("\n")
