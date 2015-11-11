# BA1F
# Find a Position in a Genome Minimizing the Skew

def skew(genome):
	skewValue = {'C':-1, 'A':0, 'T':0, 'G':1}
	resultList = []
	result = 0
	resultList.append(result)
	for nt in genome:
		result += skewValue[nt]
		resultList.append(result)
	return resultList

def findMin(skew):
	# when the list is given, find the (multiple) index of minimum value in the list
	minVal = 0
	# first, find the minimum value
	for i in skew:
		if i <= minVal :
			minVal = i
	# and then, get that index of the minimum value
	for i in range(len(skew)):
		if skew[i] == minVal:
			print i,

# read file and return a single string of dna
def SingleString(filename):
	f = open(filename)
	result = ''
	for line in f.readlines():
		line = line.strip()
		result += line
	return result

giventext = SingleString('rosalind_ba1f.txt')

findMin(skew(giventext))
