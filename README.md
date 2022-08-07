# Project-Meme-Generator
Build a python application to generate random memes by taking in user inputs through a command line and web interface.

## Main Goal of this Project
* Can write, structure and extend your code to be able to support developing large systems at scale.
* Can leverage open source open libraries to quickly add advanced functionality to your code, and can package your own code into libraries of your own. 
* Apply Object Oriendted Programming to ensure your code remains modular, clear and understandable.

## Overview 
This project is to build a python application to generate random memes by taking in user inputs through a command line and web interface.
- First, import quote data from many different data types (PDF, DOCX, CSV, TXT), and write clean, modular code to handle these different file types in Object Oriendted Programming.
- Second, resize images and overlay the quotes onto the resized graphics.
- Make service avaiable for users to use as a command line utility and as a deployable web service.

## Main Modules
[QuoteEngines](Project-Meme-Generator/tree/master/src/QuoteEngine)
[MemeGenerator](Project-Meme-Generator/tree/master/src/MemeGenerator)

## Prerequisites
Install all dependencies given in the requirements.txt file using pip: 
```bash=
pip install -r requirements.txt
```

## Uses
### Flask Web Application
This application is built with Flask. Start the application by running the following command:
```bash=
python app.py
```

### Command Line Interface
This project contains a simple cli app starter code in meme.py. The script takes three optional CLI arguments:
- `--body`:  a string quote body
- `--author`:  a string quote author
- `--path`: an image path
