# BA1M
# Implement NumberToPattern

# Convert an integer to its corresponding DNA string.
# Given: Integers index and k.
# Return: NumberToPattern(index, k).

def NumberToPattern(index, k):
	symrev = {0:'A', 1:'C', 2:'G', 3:'T'}
	result = ''
	for i in range(k):
		symnum = index/(4**(k-1-i))
		result += symrev[symnum]
		index = index - symnum*(4**(k-1-i))
	return result
