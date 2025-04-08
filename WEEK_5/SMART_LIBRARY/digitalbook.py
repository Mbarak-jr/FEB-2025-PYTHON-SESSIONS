from book import Book


class DigitalBook(Book):
    def __init__(self, title, author, publication_year, format, size, url):
        # Initialize the parent class (Book)
        super().__init__(title, author, publication_year)
        self.format = format
        self.size = size
        self.url = url
        self.downloaded = False

    def download(self):
        # Check if the digital book is available for download
        if self.available:
            self.downloaded = True
            self.available = False
            return f"{self.title} has been downloaded."
        else:
            return f"{self.title} is currently unavailable for download."

    def get_details(self):
        # Get the details from the Book class and add additional properties
        details = super().get_details()
        details.update({
            "format": self.format,
            "size": self.size,
            "url": self.url,
            "downloaded": self.downloaded,
            "type": "Digital Book"
        })
        return details
