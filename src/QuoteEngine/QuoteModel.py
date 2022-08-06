class QuoteModel():
    def __init__(self, body, author):
        # if body is not str:
        #     raise Exception('Not a string!')
        self.body = str(body)
        self.author = author