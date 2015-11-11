# BA1L
# Implement PatternToNumber

# Convert a DNA string to a number.
# Given: A DNA string Pattern.
# Return: PatternToNumber(Pattern).

def PatternToNumber(pattern):
	sym = {'A':0, 'C':1, 'G':2, 'T':3}
	k = len(pattern)
	result = 0
	for i in range(k) :
		result += sym[pattern[i]]*(4**(k-1-i))
	return result
