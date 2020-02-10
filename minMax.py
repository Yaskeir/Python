#Mateusz Fido
import random

def minMax(seq):
    '''Accepts a sequence of integers and returns the 
    largest and the smallest value, alongside their indices,
    following the pattern: value, index'''
    min = seq[0]
    max = seq[0]
    indexMin = [] # return a list of indices, as one value 
    indexMax = [] # can appear multiple times in a sequence
    for i in seq:
        if i > max:
            max = i
        elif i < min:
            min = i
    for j in range(0, len(seq)):
        if seq[j] == max:
            indexMax.append(j)
        elif seq[j] == min:
            indexMin.append(j)
    answer = "The largest value is {}, at index {}. The smallest value is {}, at index {}.".format(max, indexMax, min, indexMin)
    return min, indexMin, max, indexMax, answer

#seq1 = [5, 4, 12, 27, 8, 1, 2, 10]
#print(minMax(seq1))
seq2 = [random.randint(0,100) for i in range(15)]
print(minMax(seq2))
print("Testing:", seq2, "\nMax:", max(seq2), "at index", seq2.index(max(seq2)), "Min:", min(seq2), "at index", seq2.index(min(seq2)))