# The number of mismatches between strings p and q is called the Hamming distance between these strings and is denoted HammingDistance(p, q).

# Hamming Distance Problem: Compute the Hamming distance between two strings.
#     Input: Two strings of equal length.
#     Output: The Hamming distance between these strings.

def hamming(p, q):
	count = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			count += 1
	return count

# example
# print hamming('GGGCCGTTGGT', 'GGACCGTTGAC')
# print hamming('CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA',  'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG.')

# return the list of dna sequences from FASTA format file
def createfile(filename):
	f = open(filename)
	seq = []
	temp_str = ''
	for line in f.readlines():
	    line = line.strip()
	    if '>' not in line:
	        temp_str += line
	    else:
	        seq.append(temp_str)
	        temp_str = ''
	seq.append(temp_str)
	#seq.remove('')
	return seq

'''
givenseq = createfile('dataset_9_3.txt')

# assume that there are only 2 dna strings in the list
p1 = givenseq[0]
p2 = givenseq[-1]
print hamming(p1, p2)
'''

# compute the list of indexes of the pattern in a dna sequence
def hammingindex(pattern, genome, d):
	index = []
	for i in range(len(genome)- len(pattern)+1):
		if hamming(pattern, genome[i:i+len(pattern)]) <= d: 
			index.append(i)
	for i in index:
		print i,

'''
# example
# print hammingindex('ATTCTGGA', 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', 3)

givenseq = createfile('dataset_9_4.txt')
pattern = givenseq[0]
genome = givenseq[1]
# print hammingindex(pattern, genome, 4)
'''

def hammingcount(text, pattern, d):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if hamming(pattern, text[i:i+len(pattern)]) <= d:
			count += 1
	return count

'''
# examples
# print hammingcount('AACAAGCTGATAAACATTTAAAGAG', 'AAAAA', 1)
# print hammingcount('AACAAGCTGATAAACATTTAAAGAG', 'AAAAA', 2)
# print hammingcount('TACGCATTACAAAGCACA', 'AA', 1)
# print hammingcount('TTTAGAGCCTTCAGAGG', 'GAGG', 2)
# print hammingcount('CGTCACGTGGTGAGAAATCGTTGACGAGCTGAGGCCTCCAGAATGGTGCCAAGCGTCCTTGTGAGACACGTGTATAGCATACTGGGGCTCTCCGTCGTTCGTTGAGTCCATACCCGACGAACTAACAGTCCCGCTGGTCGGAAAATCGATTTCAAGGTTGTTTGCGATGTGCGTCTCTGTCATTACGTGTGGCCACTCCTGTGACTTATGCCATACATAAGGCTGAGGCGGGCCAGCCCTACTTCTTGCCAGTCGTCCTGACAAGTCAATTCCTTCGCTTGAGTTAAGGCTAATAGTATGGGGGGA', 'CCAGCCC', 2)
'''
# wrong output, why?
def hammingFrequentWord(text, k, d):
	freqPTs = {}
	max = 0
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		count = hammingcount(text, pattern, d)
		freqPTs[pattern] = count
		if count >= max :
			max = count
	for pt in freqPTs.keys():
		if freqPTs[pt] == max:
			print pt,	

# print hammingFrequentWord('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)
# this result came out correctly, but as the d is increasing, the fuction 'hammingFrequentWord' cannot compute correct result

def ComputingFrequencies(text, k):
    freqArray = []
    for i in range(4**k):
        freqArray.append(0)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = PatternToNumber(pattern)
        freqArray[j] = freqArray[j]+1
    return freqArray

# convert pattern to number
def PatternToNumber(pattern):
    score = {'A':0, 'C':1, 'G':2, 'T':3}
    result = 0
    tens = 0
    for nt in pattern[::-1] :
        result += (4**tens)*score[nt]
        tens += 1
    return result

# convert number to pattern with given k-mer length
def NumberToPattern(i, k):
    rescore = {0:'A', 1:'C', 2:'G', 3:'T'}
    temp = ''
    for n in range(k)[::-1]:
        temp += rescore[i/(4**n)]
        i = i-(i/(4**n))*(4**n)
    return temp

def FrequentWordsWithMismatches(Text, k, d):
        FrequentPatterns = []
        Close = [0]*(4**k)
        FrequencyArray = [0]*(4**k)
        maxCount = 0
        for i in range(len(Text)-k+1) :
            Neighborhood = Neighbors(Text[i:i+k], d)
            for Pattern in Neighborhood :
            	index = PatternToNumber(Pattern)
            	Close[index] = 1
        for i in range(4**k):
            if Close[i] == 1 :
                Pattern = NumberToPattern(i, k)
                FrequencyArray[i] = hammingcount(Text, Pattern, d)
                if FrequencyArray[i] >= maxCount :
                	maxCount = FrequencyArray[i]
        for i in range(4**k):
            if FrequencyArray[i] == maxCount :
                Pattern = NumberToPattern(i, k)
                FrequentPatterns.append(Pattern)
        return FrequentPatterns 

# this is the version of Neighbors when d == 1
def ImmediateNeighbors(Pattern):
	Neighborhood = [Pattern]
	PTlist = list(Pattern)
	for i in range(len(PTlist)) :
		symbol = PTlist[i]
		for nt in ['A', 'T', 'G', 'C']:
			if nt == symbol :
				pass
			else :
				PTlistcopy = list(Pattern)
				PTlistcopy[i] = nt
				newPT = "".join(PTlistcopy)
				if newPT not in Neighborhood:
					Neighborhood.append(newPT)			
	return Neighborhood

def Neighbors(Pattern, d):
	if d == 0 : 
		return Pattern
	elif len(Pattern) == 1 :
		return ['A', 'C', 'G', 'T']
	else :
		Neighborhood = []
		SuffixNeighbors = Neighbors(Pattern[1:], d)
		for string in SuffixNeighbors :
			if hamming(Pattern[1:], string) < d :
				for nt in ['A', 'T', 'G', 'C']:
					if nt+string not in Neighborhood :
						Neighborhood.append(nt+string)
			else:
				Neighborhood.append(Pattern[0]+string) 
		return Neighborhood

'''
f = open('dataset_3014_ans.txt', 'w')
for item in Neighbors('GCGCTAAGTGGG', 2):
	f.write(item)
	f.write('\n')
f.close()
'''
#seq = 'TGGGCTGCTCAAGCAAGGAAGCTGAAGAATGGTGGGAAGAAGCTGCTTGGCAAGCAAGCAAGCAAGCATGCATGGAAGAACATGCAAGGCTGCTTGGGCTCATGGCTCATGCAAGGCTGCTCATGGCTGCTCATGTGGGCTGAAGCTGCTTGGTGGGAACAAGCATGGCTGAAGCTCAAGCATGCATGCAAGCAAGCATGGCTCATGTGGCAAGCATGGCTGCTCAAGCAAGGCTCAAGTGGGCTCAAGTGGCATGGCTGAAGCTCATGTGGTGGCATGCAAGCAAGCAAGTGGGAAGCTTGGGAAGCTCAAGTGGCATGCATGTGGCATGTGGTGGCATGGCTCATGCAAG'
#print FrequentWordsWithMismatches(seq, 6, 3)

# compute the reverse complement of pattern, a dna string
def complement(pattern):
	DNAcomp = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	seq = ''
	for i in pattern[::-1]:		
		seq += DNAcomp[i]
	return seq

# other version of FrequentWordsWithMismatches, that return also its reverse complement sequence	
def FrequentWordsWithMismatchesReverse(Text, k, d):
        FrequentPatterns = []
        Close = [0]*(4**k)
        FrequencyArray = [0]*(4**k)
        maxCount = 0
        for i in range(len(Text)-k+1) :
            Neighborhood = Neighbors(Text[i:i+k], d)
            for Pattern in Neighborhood :
            	index = PatternToNumber(Pattern)
            	Close[index] = 1
        for i in range(4**k):
            if Close[i] == 1 :
                Pattern = NumberToPattern(i, k)
                revseq = complement(Pattern)
                FrequencyArray[i] = hammingcount(Text, Pattern, d) + hammingcount(Text, revseq, d)
                if FrequencyArray[i] >= maxCount :
                	maxCount = FrequencyArray[i]
        for i in range(4**k):
            if FrequencyArray[i] == maxCount :
                Pattern = NumberToPattern(i, k)
                FrequentPatterns.append(Pattern)
        return FrequentPatterns

#print FrequentWordsWithMismatchesReverse('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)

#print FrequentWordsWithMismatchesReverse('CAGTCCGCTGCTGCTGCTGCCAGCAGCAGCAGGCTCCGCTCCTCCGCTCAGTATACAGGCTATCCGCTGCTATCCCAGTAGCCAGGCTTCCTCCTCCGCTATATATACAGTATCCTCCGCGCTCAGCAGTAGCGCTTCCGCCAGTCCTAGCTTCCGCTTAGCTGCTTAGCGCTTCCTAGCGCCAGGCTCAGTCCTCCTCCCAGTCCGCTATCCTCCCAGTCCTCCTCC', 5, 2)

