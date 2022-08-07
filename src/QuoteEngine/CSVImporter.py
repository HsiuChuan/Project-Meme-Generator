"""Importer of csv file."""
import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVImporter(IngestorInterface):
    """Class of importing CSV file."""

    allowwd_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse rows in CSV file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        df = pd.read_csv(path)
        quotes = []
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
