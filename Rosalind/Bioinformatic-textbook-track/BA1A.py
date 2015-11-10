# Compute the Number of Times a Pattern Appears in a Text

def patternCount(text, pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern :
			count += 1
	return count
