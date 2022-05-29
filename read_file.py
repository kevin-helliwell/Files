# Reads in a file called test.txt and displays each line with a "-" added in front
dataFile = open("test.txt")
for line in dataFile:
    print("-"+line.rstrip())
dataFile.close()
