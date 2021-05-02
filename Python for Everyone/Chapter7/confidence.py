'''Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence:
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number
on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach
the end of the file, print out the average spam confidence.'''


fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File not found')
    exit()

total = 0.0
counter = 0

for line in fhandle:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # print(line)

    line = line.split()
    number = float(line[1])

    total = total + number
    counter += 1

print('Average spam confidence: ' + str(total/counter))
