"""Abstract class of ingestor."""
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class of ingestor."""

    allowwd_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Detect the file extension."""
        ext = path.split('.')[-1].lower()
        return ext in cls.allowwd_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse funciton of ingestor."""
        pass
