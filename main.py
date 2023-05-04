import csv

words = []
definitions = []
#'{\\hebrewfont\\RL{אֵב}} \\begin{english}bud\\end{english}\\\\\n'
# Open the file
with open("demo.tex", "r") as file:
    for line in file:
        # If the line has a volcabulary word
        if "{\hebrewfont\RL{" in line:
            # Get the word
            word = line.split("{\hebrewfont\RL{")[1].split("}}")[0]
            words.append(word)

            # Get the definition
            definition = line.split("{english}")[1].split("\\end")[0]
            definitions.append(definition)

# Save words and definitions to the csv file
with open("output.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Word", "Definition"])
    for i in range(len(words)):
        writer.writerow([words[i], definitions[i]])