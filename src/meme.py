"""Combine MemeGeneator & QuoteEngin."""
import os
import random
import pandas as pd

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeGenerator
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
            ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Add path, body and auther into argument')
    parser.add_argument('--path', type=str, default=None)
    parser.add_argument('--body', type=str, default=None)
    parser.add_argument('--author', type=str, default=None)

    args = parser.parse_args()
    # args = None
    print(generate_meme(args.path, args.body, args.author))
