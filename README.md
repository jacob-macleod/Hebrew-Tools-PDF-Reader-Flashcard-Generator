# Hebrew-Tools-PDF-Reader-Flashcard-Generator
**Description:** Generate .csv files for flashcards from the **LATEX** at https://reader.hebrewtools.org


- [Hebrew-Tools-PDF-Reader-Flashcard-Generator](#hebrew-tools-pdf-reader-flashcard-generator)
  - [How do I use this?](#how-do-i-use-this)
  - [What is this script?](#what-is-this-script)
  - [How much has been developed?](#how-much-has-been-developed)


## How do I use this?
* Run the python file
  * For example, with `python3 main.py`

You can supply command line arguments to tweak values. Below, you can see the argument name with a brief description.

| Argument | Description | Default value |
|----------|-------------|---------------|
|fileToReadFrom|The LATEX file that will be read from to generate the words to turn into flashcards|Defaults to  `demo.tex`|
|fileToWriteTo|The output `.csv` file produced by the code|Defaults to `output.csv`|
|mostCommonWordsFile|The file that stores the `x` most common words - *these words are **not** saved when the output `.csv` is generated.* If you want to save every value in the file to the `.csv` file, set this to a blank document|Defaults to `500MostCommon.csv`|

These values are given in the format:

`python3 main.py fileToWriteTo=myFile.txt fileToReadFrom=myOtherFile.txt`


## What is this script?

* https://reader.hebrewtools.org lets you generate PDF or LATEX files in Hebrew from passages supplied in the Hebrew Tanach (Old Testament). You can optionally create a document with the words supplied at the bottom
* This script takes the **LATEX** version, and puts all the words used in a *.csv* file
  * In addition, the code does not add the words in (by default) the `500MostCommon.csv` file.
    * If you are learning words, you don't want to be taught words you already know!
* The file contains word and definition
* This .csv file can easily be imported into programs such as Anki, to give flashcards for a specific book

## How much has been developed?
* This has been developed to a reasonable extent. While a UI has not veen developed, this is not really needed for a simple script.

