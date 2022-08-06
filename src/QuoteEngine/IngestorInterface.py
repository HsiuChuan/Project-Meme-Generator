from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    allowwd_extensions = []
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1].lower()
        return ext in cls.allowwd_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass