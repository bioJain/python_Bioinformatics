# Skewi(Genome) computest the difference between the total G and the total C in the first i nucleotides of Genome. 
# Skew0 = 0

# if i-th nt == G, skew.i = skew.i-1 + 1
# elif i-th nt == C, skew.i = skew.i-1 - 1
# else, skew.i = skew.i-1

def skew(seq):
	value = 0
	valist = [0]
	for nt in seq :
		if nt == 'C':
			value += -1
		elif nt == 'G':
			value += 1
		valist.append(value)
	'''	
	# to print all the skew value
	for item in valist:
		print item,
	'''
	min = 0
	minindex = 0
	for item in valist:
		if item <= min :
			min = item
	print 'minimum skew value is ', min,
	print 
	print 'indexes are'
	for i in range(len(valist)):
		if valist[i] == min:
			print i,

# examples
# print skew('CATGGGCATCGGCCATACGCC')
# print skew('GAGCCACCGCGATA')
# print skew('GATACACTTCCCGAGTAGGTACTG')
# print skew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')

# read a whole genome and return a single string
def createfile(filename):
	f = open(filename)
	temp_str = ''
	for line in f.readlines():
	    line = line.strip()
	    if '>' not in line:
	        temp_str += line
	return temp_str

givenseq = createfile('dataset_7_6.txt')
print skew(givenseq)
