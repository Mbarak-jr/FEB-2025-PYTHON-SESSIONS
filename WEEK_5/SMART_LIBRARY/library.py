class Library:
    def __init__(self, name):
        self.name = name
        self.items = []  # Store all items (books, digital books, magazines)

    def add_item(self, item):
        """Add any item to the library."""
        self.items.append(item)

    def remove_item(self, title):
        """Remove an item (book, digital book, or magazine) by title."""
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                return True
        return False

    def search_item(self, title):
        """Search for an item by title."""
        for item in self.items:
            if item.title == title:
                return item
        return None

    def list_items(self):
        """List all items in the library."""
        return [item.get_details() for item in self.items]

    def get_all_items(self):
        """Return details of all items in the library."""
        return [item.get_details() for item in self.items]
