import pandas as pd 
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVImporter(IngestorInterface):
    allowwd_extensions = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        df = pd.read_csv(path)
        quotes = []
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes