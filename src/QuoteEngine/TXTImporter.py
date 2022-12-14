"""Class of importing TXT file."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTImporter(IngestorInterface):
    """Class of importing TXT file."""

    allowwd_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse rows in TXT file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        Quotes = []
        f = open(path, 'r', encoding="utf-8")
        for line in f.readlines():
            line = line.encode("latin-1").decode("utf-8") #.encode("utf-8").decode("latin1")
            parse = line.split('-')
            new_quote = QuoteModel(parse[0].strip(), parse[1].strip())
            Quotes.append(new_quote)
        
        return Quotes