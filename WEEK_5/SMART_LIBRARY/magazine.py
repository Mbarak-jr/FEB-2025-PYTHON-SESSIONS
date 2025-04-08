from book import Book

class Magazine(Book):
    def __init__(self, title, author, publication_year, issue_number):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number

    def get_details(self):
        details = super().get_details()
        details["issue_number"] = self.issue_number
        return details