"""Combine all file importers as a ingestor."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter


class Ingestor(IngestorInterface):
    """Class of all ingestor."""
    
    importers = [CSVImporter, DocxImporter, TXTImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all the kind of files."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
