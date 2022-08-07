"""Importer of DOCX file."""
# pip install -U setuptools
# pip install python-docx
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    """Class of importing DOCX file."""

    allowwd_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse rows in DOCXß file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        Quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                Quotes.append(new_quote)
        return Quotes
