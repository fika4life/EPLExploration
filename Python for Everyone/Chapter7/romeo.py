fname = input("Enter file: ")

try:
    fhandle = open(fname)
except:
    print('File not found')
    exit()

uniqueWords = []

for line in fhandle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        if word not in uniqueWords:
            uniqueWords.append(word)

print(sorted(uniqueWords))
