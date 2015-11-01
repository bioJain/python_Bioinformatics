# Python for Genomic Data Science (class_Coursera_JOHNS HOPKINS)
# this is the Final Exam python scripts 

# Given: A collection of DNA strings in FASTA format 
# Output : compute answers for each question 

# to see the answer of the each question, del. the '#' ahead of function calls

# read data from the FASTA format, and re-organize it as the dictionary
def createdic(filename):
    f = open(filename, 'r')
      
    mapping = {}
      
    last_key = ''
    temp_str = ''
 
    for line in f.readlines():
        line = line.strip() #.replace('\r\n', '')
        if line.startswith(">"):
            if len(last_key) != 0:
                mapping[last_key] = temp_str
                temp_str = ''   
            new_line = line.replace('>', '');
            last_key = new_line
        else:
            temp_str += line
    mapping[last_key] = temp_str
 
    return mapping

# create dic with the identifier as a key and the dna string as a value
dicname = createdic('dna4.fasta')

# 1. how many records? // count the number of dna strings or identifiers
# Q1. answer
# print len(dicname.keys())

# Q2-3. length of the sequences
# fuction 'count' computes the longest and shortest length among dna strings
def count(dic) :
    longest = len(dic.values()[0])
    shortest = len(dic.values()[0])
    for i in dic.values():
        if len(i) >= longest :
            longest = len(i)
        elif len(i) <= shortest:
            shortest = len(i)
    print 'longest length is ', longest
    print 'shortest length is ', shortest
# Q2 and Q3. answers
# count(dicname)

# 4-6. find ORF
codonTable = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 
'CUC':'L', 'AUC':'I', 'GUC':'V', 'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V', 'UCU':'S', 'CCU':'P', 'ACU':'T',
'GCU':'A', 'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A', 'UCA':'S', 'CCA':'P',
'ACA':'T', 'GCA':'A', 'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A', 'UAU':'Y', 
'CAU':'H', 'AAU':'N', 'GAU':'D', 'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E', 'UAG':'Stop', 'CAG':'Q', 'AAG':'K',
'GAG':'E', 'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R',
'AGC':'S', 'GGC':'G', 'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}

# function 'translation' translate DNA string into amino acid chain 
def translation(seq):
    rnaseq = seq.replace('T', 'U')
    codon = ''
    AA = ''
    aalist = []
    for nt in rnaseq :
        codon += nt
        if len(codon) == 3:
            if codon == 'AUG':
                AA += codonTable[codon]
            elif codonTable[codon] == 'Stop' and AA != '':
                aalist.append(AA)
                AA = ''
            elif AA != '' :
                AA += codonTable[codon]
            codon = ''
    return aalist

# 4-5. longest ORF in reading frame 1,2,3

# longest ORF length is based on 'DNA string length'
# so, *3 to the length of 'Amino acid chain'
# and the +3 to count the length of 'stop codon'

def ORFlen(dicname):
    for i in range(3):
        resultlist = []
        longest = 0
        for string in dicname.values():
            templist = translation(string[i:])
            for aa in templist :
                resultlist.append(aa)
                if len(aa)>= longest:
                    longest=len(aa)
        print 'longest length of ORF', i+1, 'is', longest*3+3

# Q4-5. answer // find the longest ORF length in all DNA strings
# print ORFlen(dicname)

def ORFlen2(keyname, dicname):
    for i in range(3):
        resultlist = []
        longest = 0
        for string in dicname.keys():
            if keyname in string :
                templist = translation(dicname[string][i:])
                for aa in templist :
                    resultlist.append(aa)
                    if len(aa)>= longest:
                        longest=len(aa)
        print 'longest length of ORF', i+1, 'is', longest*3+3

# Q6. answer // find the longest ORF length within the given identifier
# print ORFlen2('gi|142022655|gb|EQ086233.1|349', dicname)


# Q7-9. most frequently occurring pattern repeats
# count the pattern(substring) in a given dna
def patternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

# find the most frequent patterns(substring) of length k in all given dna
# answer can be several patterns
def frequentWord(dicname, k):
    totalPTs = {}
    max = 0
    for text in dicname.values():
        freqPTs = {}
        for i in range(len(text)-k+1):
            pattern = text[i:i+k]
            if pattern in freqPTs.keys():
                pass
            else :
                count = patternCount(text, pattern)
                freqPTs[pattern] = count
        for pt in freqPTs.keys():
            totalPTs[pt] = totalPTs.get(pt, 0) + freqPTs[pt]
    for pt in totalPTs.keys():
        if totalPTs[pt] >= max:
            max = totalPTs[pt]
    for pt in totalPTs.keys():
        if totalPTs[pt] == max:
            print pt, 
            print max

        
# Q7. find the most frequently occurring repeat of length 6 in all sequences, and how many times
# print frequentWord(dicname, 6) 

# Q8. how many different seq. of length 11. occurring max time
# print frequentWord(dicname, 11) 

# Q9. find the most frequent repeat sequence of  length 7
# print frequentWord(dicname, 7) 
