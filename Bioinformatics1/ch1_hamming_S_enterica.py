import hamming
import skew

# read the whole genome and store it
S_enterica=skew.createfile('Salmonella_enterica.txt')

# calculate the minimum skew value of Salmonella enterica
skew.skew(S_enterica)

# To find the DnaA box in Salmonella enterica
# give 1000-bp wide range as the minimum skew index at the center
# 9-mer (k = 9)
# with hamming distance = 1
print hamming.FrequentWordsWithMismatchesReverse(S_enterica[3764856-500:3764856+500], 9, 1)


