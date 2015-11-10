# BA1C
# Find the Reverse Complement of a String

# read file and return a single string of dna
def SingleString(filename):
	f = open(filename)
	result = ''
	for line in f.readlines():
		line = line.strip()
		result += line
	return result

# compute the reverse complementation of a given dna 
def ReverseComplement(pattern):
	ntDic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	result = ''
	for nt in pattern[::-1]:
		result += ntDic[nt]
	return result

# create the answer as the file form
def writeAns(answer, filename):
	f = open(filename, 'w')
	for i in answer:
		f.write(i)
	f.close()
