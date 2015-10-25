# count the pattern(substring) in a given dna
def patternCount(text, pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

# find the most frequent pattern(substring) of length k in a given dna
def frequentWord(text, k):
	freqPTs = {}
	max = 0
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		count = patternCount(text, pattern)
		freqPTs[i] = count
		if count >= max :
			max = count
			mostPT = pattern
	return mostPT

print patternCount('ACTGTACGATGATGTGTGTCAAAG', 'TGT')
print frequentWord('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3)
