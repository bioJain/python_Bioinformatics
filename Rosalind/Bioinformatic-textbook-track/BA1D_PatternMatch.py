# BA1D
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
