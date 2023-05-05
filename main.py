import csv, re, sys

class Volcabulary:
    def __init__(self, fileToWriteTo = "output.csv", fileToReadFrom = "demo.tex", mostCommonWordsFile = "500MostCommon.csv") :
        # Initialise variables
        self.words = []
        self.definitions = []
        self.mostCommonWords = []
        self.mostCommonDefinitions = []
        self.fileToWriteTo = fileToWriteTo
        self.fileToReadFrom = fileToReadFrom
        self.mostCommonWordsFile = mostCommonWordsFile
        self.vowel_pattern = re.compile(r"[\u0591-\u05C7]")

    # Remove vowels from the word when comparing it against the most common words
    def removeVowels(self, text: str) -> str:
        return re.sub(self.vowel_pattern, "", text)
        
    def storeMostCommonWords(self) :

        # Store the most common words and definitions from the csv file
        try :
            with open (self.mostCommonWordsFile, "r") as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    self.mostCommonWords.append(line[0])
                    self.mostCommonDefinitions.append(line[1])
        except :
            print ("Error: Most common words file not found")

    # Store the words and definitions used in the text file supplied to variables
    def storeWordsAndDefinitionsInTextFile(self) :
        # Open the file
        try:
            with open(self.fileToReadFrom, "r") as file:
                for line in file:
                    wordUsed = False
                    # If the line has a volcabulary word
                    if "{\hebrewfont\RL{" in line:
                        # Get the word
                        word = line.split("{\hebrewfont\RL{")[1].split("}}")[0]

                        # Get the definition
                        definition = line.split("{english}")[1].split("\\end")[0]

                        # If the word isn't in the most common words
                        # This works even if the descriptions are different, which may happen, or if two
                        # words have the same description but are different words
                        for mostCommonWord in self.mostCommonWords:
                            if self.removeVowels(word) == self.removeVowels(mostCommonWord):
                                wordUsed = True
                        
                        if wordUsed == False:
                            self.definitions.append(definition)
                            self.words.append(word)
        except:
            print ("Error: File to read from not found")

    # Write the words and definitions generated to a text file
    def writeToFile(self) :
        # Save words and definitions to the csv file
        with open(self.fileToWriteTo, "w") as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(self.words)):
                writer.writerow([self.words[i], self.definitions[i]])

    def run(self) :
        self.storeMostCommonWords()
        self.storeWordsAndDefinitionsInTextFile()
        self.writeToFile()
        
        print ("Execution complete")


# Run the code
if __name__ == '__main__':
    # Parse command-line arguments
    args = {}
    for arg in sys.argv[1:]:
        key, value = arg.split('=')
        args[key] = value

    # Initialize Vocabulary class with supplied arguments
    vocabulary = Volcabulary(**args)

    # Run the vocabulary processing
    vocabulary.run()