# Catalan numbers

# Works for any number of Catalan terms, 
# But constrained to numbers below 1 million

def catalanNumbers(n):
    #create placeholder variables for a list of numbers, 
    #the current term and an even/odd number counter
    catalanList = []
    currentTerm = 1
    evenCounter = 0
    #handle the edge case
    if n == 0:
        return currentTerm, "1 odd term, no even terms"
    else:
        #append to the list and apply the recursive formula
        for i in range (0, n):
            catalanList.append(currentTerm)
            currentTerm = int((4*i+2)/(i+2) * currentTerm)
            if currentTerm > 1000000:
                break
    #iterate over the list and find the number of evens and odds
    for i in catalanList:
        if i % 2 == 0:
            evenCounter += 1
    oddsAndEvens = "even terms: " + str(evenCounter) + ", odd terms: " + str(len(catalanList) - evenCounter)
    return catalanList, oddsAndEvens

print(catalanNumbers(30))
#print(catalanNumbers(20))
#print(catalanNumbers(10))
#print(catalanNumbers(0))
