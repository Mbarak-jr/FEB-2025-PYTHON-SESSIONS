from library import Library
from book import Book
from digitalbook import DigitalBook
from magazine import Magazine


def main():
    # Create a library instance
    library = Library("My Library")

    # Create some book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("1984", "George Orwell", 1949)

    # Create some digital book instances
    digital_book1 = DigitalBook(
        "Digital Fortress", "Dan Brown", 1998, "PDF", "10MB", "http://example.com/digital_fortress"
    )
    digital_book2 = DigitalBook(
        "The Da Vinci Code", "Dan Brown", 2003, "EPUB", "15MB", "http://example.com/da_vinci_code"
    )

    # Create some magazine instances
    magazine1 = Magazine("National Geographic",
                         "National Geographic Society", 2023, "0012-0986")
    magazine2 = Magazine("TIME", "Time USA, LLC", 2023, "0040-781X")

    # Add items to the library using add_item
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(digital_book1)
    library.add_item(digital_book2)
    library.add_item(magazine1)
    library.add_item(magazine2)

    # Display all items in the library
    print("📚 All items in the library:")
    for item in library.get_all_items():
        print(item)


# 👇 This runs main() when script is executed
if __name__ == "__main__":
    main()
