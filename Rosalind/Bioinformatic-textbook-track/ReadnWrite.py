# These are the functions for reading and writing files.

# read the dna as a single string except the last line(usually containing other information than dna)
def readExcLast(readfilename):
	f = open(readfilename)
	read = ''
	for line in f.readlines()[:-1]:
		line = line.strip()
		read += line
	return read

# read through the variable and write it as a file with a space interval
# you can change the interval to blank line by '\n'
def writeAns(filename, variable):
	f = open(filename, 'w')
	for i in variable :
		f.write(i)
		f.write(' ')
	f.close()


