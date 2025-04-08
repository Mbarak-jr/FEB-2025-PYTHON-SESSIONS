class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = True  # Ensure the 'available' attribute is initialized

    def borrow(self):
        if self.available:
            self.available = False
            return f"{self.title} has been borrowed."
        else:
            return f"{self.title} is currently unavailable."

    def return_book(self):
        self.available = True
        return f"{self.title} has been returned."

    def get_details(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "available": self.available
        }
