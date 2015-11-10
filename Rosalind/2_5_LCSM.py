# LCSM : Finding a Shared Motif

# Given: A collection of k (k<=100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# read data from the FASTA format, and re-organize it
def createdic(filename):
    fn = filename + '.txt'
    f = open(fn, 'r')
      
    dnalist = []
    temp_str = ''
 
    for line in f.readlines():
        line = line.strip() #.replace('\r\n', '')
        if line.startswith(">"):
            if len(temp_str) != 0:
                dnalist.append(temp_str)
                temp_str = ''   
        else:
            temp_str += line
    dnalist.append(temp_str)
    return dnalist

# 1. among given dnas, find the shortest.

LCSMlist = createdic('rosalind_lcsm')

def shortest(givenlist):
	mindna = len(givenlist[0])
	giventext = givenlist[0]
	for dna in givenlist :
		if len(dna) <= mindna:
			mindna = len(dna)
			giventext = dna
	return giventext

# find the most frequent patterns(substring) of length k in a given dna
# answer can be several patterns
def sharedWord(text, givenlist):
	sharedPTs = {}
	PTlist = []
	kmax = len(text)
	kmin = 0
	k = (kmax + kmin)/2
	while k > 1 :
		print k
		if k in sharedPTs.keys():
			return sharedPTs
		
		PTlist = []
		for i in range(len(text)-k+1):
			count = 0
			pattern = text[i:i+k]
			if pattern in PTlist :
				pass
			else :
				for dna in givenlist :
					if pattern not in dna :
						break
					else :
						count += 1
				if count == len(givenlist) :
					PTlist.append(pattern)
		sharedPTs[k] = PTlist
		if len(PTlist) == 0 :
			kmax = k			
			k = (kmax + kmin)/2
		elif (kmax-kmin) <= 2 :
			return sharedPTs
		else :
			kmin = k
			k = (kmax + kmin)/2

LCSMtext = shortest(LCSMlist)
LCSMdic = sharedWord(LCSMtext, LCSMlist)

def singlePT(givendic) :
	longlen = 0
	longpt = ''
	for patternlist in givendic.values():
		if len(patternlist) == 0 :
			pass
		else :
			for pattern in patternlist :
				if len(pattern) >= longlen:
					longlen = len(pattern)
					longpt = pattern
	return longpt

print singlePT(LCSMdic)
