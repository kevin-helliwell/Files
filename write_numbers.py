# Asks user for name of file
# Repeatedly asks user to enter a number, entering "0" when finished
# Outputs each number to the file on a separate line

fileNamePrompt = "Please enter the name of a file.\n"
fileName = input(fileNamePrompt)
dataFile = open(fileName, "w")

numberPrompt = "Please enter a number (Enter 0 to finish).\n"
number = ""

while number != "0":
    number = input(numberPrompt)
    if number != "0":
        print(number, file=dataFile)
dataFile.close()
