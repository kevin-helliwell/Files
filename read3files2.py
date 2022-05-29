# Similar to read3_files.py but counts *WORDS* as well.


fileNames = ["test1.txt", "test2.txt", "test3.txt"]

dataFileCount = open("counts.txt", "w")

total_lines = 0
total_words = 0

for file in fileNames:
    num_lines = 0
    num_words = 0
    dataFile = open(file)

    for line in dataFile:
        num_lines += 1
        num_words += len(line.split(" "))
    dataFile.close()
    print(f"{file} : {num_lines} lines, {num_words} words", file=dataFileCount)

    total_lines += num_lines
    total_words += num_words


print(f"TOTAL: {total_lines} lines, {total_words} words", file=dataFileCount)
dataFileCount.close()
