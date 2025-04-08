from book import Book
from digitalbook import DigitalBook


def test_digital_book_initialization():
    # Test initialization of DigitalBook with valid parameters
    book = DigitalBook("Digital Book Title", "Author Name",
                       2023, "PDF", 5.0, "https://example.com/digitalbook")

    # Assertions
    assert book.title == "Digital Book Title"
    assert book.author == "Author Name"
    assert book.publication_year == 2023
    assert book.format == "PDF"
    assert book.size == 5.0
    assert book.url == "https://example.com/digitalbook"
    assert book.available == True
    assert book.downloaded == False

    # Print result
    print("✅ test_digital_book_initialization passed.")
    print(f"Initialized book: {book.get_details()}\n")


def test_digital_book_get_details():
    # Test get_details method of DigitalBook
    book = DigitalBook("Digital Book Title", "Author Name",
                       2023, "PDF", 5.0, "https://example.com/digitalbook")
    details = book.get_details()

    # Assertions
    assert details["title"] == "Digital Book Title"
    assert details["author"] == "Author Name"
    assert details["publication_year"] == 2023
    assert details["format"] == "PDF"
    assert details["size"] == 5.0
    assert details["url"] == "https://example.com/digitalbook"
    assert details["available"] == True
    assert details["downloaded"] == False
    assert details["type"] == "Digital Book"

    # Print result
    print("✅ test_digital_book_get_details passed.")
    print(f"Book details: {details}\n")


# Run the tests
test_digital_book_initialization()
test_digital_book_get_details()
