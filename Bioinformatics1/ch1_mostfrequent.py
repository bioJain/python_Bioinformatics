# count the pattern(substring) in a given dna
def patternCount(text, pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

# find the most frequent patterns(substring) of length k in a given dna
# answer can be several patterns
def frequentWord(text, k):
	freqPTs = {}
	PTlist = []
	max = 0
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		count = patternCount(text, pattern)
		freqPTs[pattern] = count
		if count >= max :
			max = count
	for pt in freqPTs.keys():
		if freqPTs[pt] == max:
			print pt,	

print patternCount('ACTGTACGATGATGTGTGTCAAAG', 'TGT')
print frequentWord('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3)
