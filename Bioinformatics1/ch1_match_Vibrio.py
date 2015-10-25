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

# read a dna string from a text file : FASTA format
def string(file):	
	f = open(file, 'r')
	dna = ''
	for line in f.readlines():
		line = line.strip()
		dna += line
	return dna

givenPT = 'CTTGATCAT'
givenDNA = string('Vibrio_cholerae.txt')

# return indexes of the pattern in a dna string
f = open('Vibrio_cholerae_ans.txt', 'w')
for i in match(givenPT, givenDNA):
	f.write(str(i))
	f.write(' ')
f.close()
