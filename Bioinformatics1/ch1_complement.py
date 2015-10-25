# compute the reverse complement of pattern, a dna string
def complement(pattern):
	DNAcomp = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	seq = ''
	for i in pattern[::-1]:		
		seq += DNAcomp[i]
	return seq

# read dna string from a text file : FASTA format
def string(file):	
	f = open(file, 'r')
	dna = ''
	for line in f.readlines():
		line = line.strip()
		dna += line
	return dna

given = string('dataset_3_2.txt')

# return a reverse complement sequence of a given dna in a text file
f = open('dataset_3_2_ans.txt', 'w')
f.write(complement(given))
f.close()
