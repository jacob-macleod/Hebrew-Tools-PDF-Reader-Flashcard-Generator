import csv, re

words = []
definitions = []
mostCommonWords = []
mostCommonDefinitions = []

vowel_pattern = re.compile(r"[\u0591-\u05C7]")

# Remove vowels from the word when comparing it against the most common words
def removeVowels(text: str) -> str:
    return re.sub(vowel_pattern, "", text)

# Store the most common words and definitions from the csv file
with open ("500MostCommon.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        mostCommonWords.append(line[0])
        mostCommonDefinitions.append(line[1])

# Open the file
with open("demo.tex", "r") as file:
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
            for mostCommonWord in mostCommonWords:
                if removeVowels(word) == removeVowels(mostCommonWord):
                    wordUsed = True
            
            if wordUsed == False:
                definitions.append(definition)
                words.append(word)

# Save words and definitions to the csv file
with open("output.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(words)):
        writer.writerow([words[i], definitions[i]])