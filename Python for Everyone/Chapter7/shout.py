
# Write a program to read through a file and print the contents of the file (line by line) all in upper case.
fname = input('Enter a file name ')
try:
    fhandle = open(fname)
except:
    print('File not found')
    exit()


for line in fhandle:
    line = line.rstrip()
    print(line.upper())
