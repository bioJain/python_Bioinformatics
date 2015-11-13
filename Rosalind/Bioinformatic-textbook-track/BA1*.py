from ReadnWrite import *

# Compute the Number of Times a Pattern Appears in a Text
def patternCount(text, pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern :
			count += 1
	return count
	
# Find the Most Frequent Words in a String
def FrequentWord(text, k):
	frequentPT = {}
	maxcount = 0
	for i in range(len(text)-k+1):		
		temp_pattern = text[i:i+k]
		if not temp_pattern in frequentPT.keys():
			temp_count = patternCount(text, temp_pattern)
			frequentPT[temp_pattern] = temp_count
			if temp_count >= maxcount :
				maxcount = temp_count
	for key in frequentPT.keys():
		if frequentPT[key] == maxcount:
			print key, 

# Find the Reverse Complement of a String
# compute the reverse complementation of a given dna 
def ReverseComplement(pattern):
	ntDic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	result = ''
	for nt in pattern[::-1]:
		result += ntDic[nt]
	return result

# Find All Occurrences of a Pattern in a String 
def PatternMatch(pattern, genome):
	matchList = []
	i = 0
	while i <= len(genome)-len(pattern) :
		j = genome.find(pattern, i)
		if j == -1 :
			break
		else :
			matchList.append(j)
			i = j+1
	return matchList

# BA1E
# Find Patterns Forming Clumps in a String

# Find patterns forming clumps in a string.
# Given: A string Genome, and integers k, L, and t.
# Return: All distinct k-mers forming (L, t)-clumps in Genome.

# make FrequencyArray
def ComputingFreq(text, k):
	FreqArray = [0] * (4**k)
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		j = PatternToNumber(pattern)
		FreqArray[j] = FreqArray[j]+1
	return FreqArray

def BetterClumpFinding(Genome, k, L, t):
	FrequentPatterns = []
	Clump = [0]*(4**k)
	Text = Genome[0:L]
	FrequencyArray = ComputingFreq(Text, k)
	for i in range(4**k):
		if FrequencyArray[i] >= t:
			Clump[i] = 1
	for i in range(1, len(Genome)-L+1):
		FirstPattern = Genome[i-1 : i-1+k]
		index = PatternToNumber(FirstPattern)
		FrequencyArray[index] = FrequencyArray[index] - 1
		LastPattern = Genome[i+L-k : i+L]
		index = PatternToNumber(LastPattern)
		FrequencyArray[index] = FrequencyArray[index] + 1
		if FrequencyArray[index] >= t :
			Clump[index] = 1
	for i in range(4**k):
		if Clump[i] == 1 :
			Pattern = NumberToPattern(i, k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns

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

# Compute the Hamming Distance Between Two Strings
def hamming(s1, s2):
	hd = 0
	for i in range(len(s1)):
		if s1[i] != s2[i] :
			hd += 1
	return hd

# Find All Approximate Occurrences of a Pattern in a String
def PatternMatchWithMis(pattern, text, d):
	startingIndex = []
	for i in range(len(text)-len(pattern)+1):
		pattern2 = text[i:i+len(pattern)]
		if hamming(pattern, pattern2) <= d:
			startingIndex.append(i)
	return startingIndex

# Find the Most Frequent Words with Mismatches in a String
def FreqWordWithMis(text, k, d):
	Set = {}
	maxcount = 0
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		Neighborpattern = Neighbors(pattern, d)
		for pt in Neighborpattern :
			Set[pt] = Set.get(pt, 0) + 1
			if Set[pt] >= maxcount :
				maxcount = Set[pt]
	for i in Set.keys():
		if maxcount == Set[i] :
			print i,

# compute the set of all k-mers whose Hamming distance from pattern does not exceed d
def Neighbors(pattern, d):
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return ['A', 'C', 'G', 'T']
	Neighborhood = []
	SuffixNeighbors = Neighbors(pattern[1:], d)
	for text in SuffixNeighbors :
		if hamming(pattern[1:], text) < d :
			for nt in ['A', 'C', 'G', 'T']:
				Neighborhood.append(nt+text)
		else :
			Neighborhood.append(pattern[0]+text)
	return Neighborhood
