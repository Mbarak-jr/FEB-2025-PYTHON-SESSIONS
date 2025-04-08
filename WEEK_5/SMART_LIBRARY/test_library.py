from library import Library

lib = Library("Test Library")
lib.add_book("1984", "George Orwell", 1949)
lib.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
lib.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print("Books in the library:")
for book in lib.list_books():
    print(
        f"Title: {book['title']}, Author: {book['author']}, Year: {book['publication_year']}, Available: {book['available']}")

print("\nSearching for '1984':")
book = lib.search_book("1984")
if book:
    print(book.get_details())
else:
    print("Book not found.")
