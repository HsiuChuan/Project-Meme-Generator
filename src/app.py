import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeGenerator


app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    # quotes from different files
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                './_data/DogQuotes/DogQuotesDOCX.docx',
                './_data/DogQuotes/DogQuotesPDF.pdf',
                './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    # dog images
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs

quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    if quote and img:
        path = meme.make_meme(img, quote.body, quote.author)
        return render_template('meme.html', path=path)
    else:
        path = meme.make_meme('./_data/photos/dog/xander_1.jpg', "Default quote.", "Default author.")
        return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    img = requests.get(image_url)
    path = None

    try:
        img_tmp_path = f'./{random.randint(0, 100)}.jpg'
        with open(img_tmp_path) as f:
            f.write(img.content)
    except:
        print("Somehting wrong with image")
        path = meme.make_meme('./_data/photos/dog/xander_1.jpg', "Default quote.", "Default author.")
    else:
        path = meme.make_meme(img_tmp_path, body, author)
        os.remove(img_tmp_path)
    finally: 
        return render_template('meme_form.html', path=path)


if __name__ == "__main__":
    app.run()
