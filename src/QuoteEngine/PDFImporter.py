from typing import List
import subprocess
import os
import random
import re


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFImporter(IngestorInterface):
    allowwd_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        Quotes = []
        tmp = f'./{random.randint(0,100000000)}.txt'       
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, "r", encoding='utf-8-sig')
  
        lines, authors, bodys = [], [], []
        for line in file_ref.readlines():
            line = line.strip()
            if len(line) > 0:
                lines.append(line)
                authors.extend(re.findall('- (.*?) ', line))
                bodys.extend(re.findall(r'"(.+?)"',line))


        quotes = list(zip(bodys, authors))
        for quote in quotes:
            new_quote = QuoteModel(quote[0].strip(), quote[1].strip())
            Quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        
        return Quotes