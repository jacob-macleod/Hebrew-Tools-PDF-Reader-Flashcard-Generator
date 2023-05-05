# Hebrew-Tools-PDF-Reader-Flashcard-Generator
**Description:** Generate .csv files for flashcards from the **LATEX** at https://reader.hebrewtools.org

## What is this script?

* https://reader.hebrewtools.org lets you generate PDF or LATEX files in Hebrew from passages supplied in the Hebrew Tanach (Old Testament). You can optionally create a document with the words supplied at the bottom
* This script takes the **LATEX** version, and puts all the words used in a *.csv* file
  * The file contains word and definition
* This .csv file can easily be imported into programs such as Anki, to give flashcards for a specific book

## How much has been developed?
* At the moment, this is a simple early version - I want to make it slightly more complicated soon
* For example, I want to make it so you have the option to not generate words that are in a list that you have supplied
* I also need to add command line arguments to make it easier to make tweak the code

## How do I use this?
* Run the python file, changing code as needed. My next aim is to add command line arguments so you can set everything up, but till then, you'll have to tweak values manually in the code
