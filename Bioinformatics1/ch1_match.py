# compute the list of indexes of the pattern in a dna sequence
def match(pattern, genome):
	i = 0
	index = []
	while i >= 0 :
		i = genome.find(pattern, i)
		index.append(i)
		i = i+1
		if i == 0 :
			break
	index.remove(-1)
	return index 

# example
# answer is 1 3 9
print match('ATAT', 'GATATATGCATATACTT')

# read a pattern and a dna string from a text file : FASTA format
# the first line is a pattern string : function pattern()
# and the rest lines are a dna string : function string()
def pattern(file):	
	with open(file, 'r') as f :
		firstline = f.readline()
		firstline = firstline.strip()
	return firstline

def string(file):	
	f = open(file, 'r')
	dna = ''
	for line in f.readlines()[1:]:
		line = line.strip()
		dna += line
	return dna

givenPT = pattern('dataset_3_5.txt')
givenDNA = string('dataset_3_5.txt')

# return indexes of the pattern in a dna string
f = open('dataset_3_5_ans.txt', 'w')
for i in match(givenPT, givenDNA):
	f.write(str(i))
	f.write(' ')
f.close()
