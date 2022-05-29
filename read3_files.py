fileNames = ["test1.txt", "test2.txt", "test3.txt"]

dataFileCount = open("counts.txt", "w")

for file in fileNames:
    num_lines = 0
    dataFile = open(file)
    for line in dataFile:
        num_lines += 1
    dataFile.close()
    print(file, ":", num_lines, file=dataFileCount)

dataFileCount.close()
