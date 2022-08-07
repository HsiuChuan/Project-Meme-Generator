"""Class of Quote Model."""

class QuoteModel():
    """Class of Quote Model."""

    def __init__(self, body, author):
        """Take in body & author."""
        # if body is not str:
        #     raise Exception('Not a string!')
        self.body = str(body)
        self.author = author
