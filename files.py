# Practice with files and dictionaries
# Count the number of letter grades in a file
# using a dictionary
# by Kevin Helliwell

letters = ["A", "B", "C", "D", "F"]
counts = {}
file = "letter-grades.txt"

# loop through all lines in the file
for line in open(file):
    letter = line.replace("\n", "")
    # if commas, use split
    # print(line)
    count = counts.get(letter, 0)  # gets the count of letter if it exists, 0 otherwise
    counts[letter] = count + 1  # store count

# Print out counts
print("Letter counts: ")
for l in letters:
    print(l+":", counts.get(l, 0))

