#!/usr/bin/env python3

class Book:
    """Represents a book with a title and page count."""

    def __init__(self, title: str, page_count: int):
        self.title = title
        self._page_count = None  # Initialize _page_count attribute

        # Set page_count using property setter
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        