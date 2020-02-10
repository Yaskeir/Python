# Script for evaluating the sequence length,
# its reverse compliment and RNA sequence
def seqLength(sequence):
    #sequence = str(input("Sequence to be evaluated for length:"))
    counter = 0
    for i in sequence:
        counter += 1
    print(counter)

def reverseCompliment(sequence):
    reversed = sequence.upper()[::-1]
    reversedList = []
    for i in reversed:
        if i == "A":
            reversedList.append("T")
        elif i == "G":
            reversedList.append("C")
        elif i == "C":
            reversedList.append("G")
        elif i == "T":
            reversedList.append("A")
        elif i == "U":
            reversedList.append("A")
        else:
            reversedList.append("X")
        reversedComplimented = "".join(reversedList)
    print(reversedComplimented) 

def dnaToRNA(sequence):
    RNA = sequence.upper()
    RNAList = []
    for i in RNA:
        if i == "T":
            RNAList.append("U")
        else:
            RNAList.append(i)
    RNA = "".join(RNAList)
    print(RNA)
    print("Don't forget to add the promoter sequence!")

def starterMethod():
    print("Welcome to the sequence calculator.")
    sequence = str(input("Please enter your sequence:"))
    return sequence


def choice(sequence):
    print("l - sequence length, r - reverse compliment, d - DNA to RNA, m - molecular weight")
    while True:
        choice = input("Now please choose your operation:")
        if choice.lower() == "l":
            seqLength(sequence)
        elif choice.lower() == "r":
            reverseCompliment(sequence)
        elif choice.lower() == "d":
            dnaToRNA(sequence)
        elif choice.lower() == "m":
            molecularWeight(sequence)
        else:
            return None
        choice2 = input("Would you like to perform another operation? y/n:")
        if choice2.lower() == "y":
            continue
        else:
            exit()


def molecularWeight(sequence):
    #mass = sequence.upper
    M = 0
    for i in sequence:
        if i == "A":
            M += 347.2
        elif i == "G":
            M += 363.2
        elif i == "C":
            M += 323.2
        elif i == "U":
            M += 324.2
        else:
            pass
    print(round(M, 2), "g/mol")

choice(starterMethod())
input("Press ENTER to exit.")