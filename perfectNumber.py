# Perfect numbers
# Checks whether a given natural number is perfect
# That is, if it is equal to the sum of all of its 
# divisors, excluding itself

def perfectNumber():
    sum = 0
    n = int(input("Please provide the natural number to be checked for perfection: "))
    while n <= 0:
        print("The number has to be a positive integer.")
        n = int(input("Please retry: "))
    for i in range(1, n): #check for every number up to (but not including) the given one
        if n % i == 0:
            sum += i      #if a divisor is found, add it to a placeholder sum
    if sum == n:          #check whether the sum of the divisors equals the number
        print(n, "is a perfect number!")
    else:
        print(n, "is not perfect.")

perfectNumber()
