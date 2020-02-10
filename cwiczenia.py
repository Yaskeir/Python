# String method .format()
import math
import random
import timeit
import os 
#import matplotlib

'''
x = 5
y = 10

if y % x == 0:
    print("y is divisible by x")

if x and y:
    print(x)
'''

'''
radius = float(input("Provide the radius: "))

if radius <= 0:
    print("Please provide a valid radius value (greater than 0).")
else:
    circleArea = radius**2 * math.pi
    print("The circle area is {:.2f}".format(circleArea))
    circleCircumference = radius * 2 * math.pi
    print("The circle circumference is {:.2f}".format(circleCircumference)) 
'''

# zad. 5, calculating a quadratic equation

'''
print("Please provide the quadratic equation coefficients.")
a = float(input("Coefficient a: "))
b = float(input("Coefficient b: "))
c = float(input("Coefficient c: "))

def quadraticEquationCalculator(a, b, c):
    if a != 0:
        delta = b**2 - 4 * a * c
        if delta < 0:
            print("Imaginary solution.")
        else: 
            x_1 = (-b - math.sqrt(delta))/(2 * a)
            x_2 = (-b + math.sqrt(delta))/(2 * a)
            print("x1 = {:.2f}".format(x_1))
            print("x2 = {:.2f}".format(x_2))
    elif b != 0:
        x = -c / b
        print("x = {:.2f}".format(x))
    elif c != 0:
        x = -c
        print("x = {:.2f}".format(x))
    else:
        print("Identity equation.")

# quadraticEquationCalculator(a, b, c)
'''
# zad 6 

'''
sum = 0
while (sum < 10):
    sum += 2
print(sum)
'''
'''
# zad 7, guessing game 

def guessingGame():
    randomNumber = random.randint(0, 10)
    print("A number between 0 and 10 (both included) has been randomly drawn.")
    guess = int(input("Your guess: "))
    while True:
        if guess == randomNumber:
            print("Congratulations! You've guessed it. The number was", randomNumber)
            break
        else:
            guess = int(input("Wrong. Try again: "))

guessingGame()
'''
'''
#range(start, end, step) -> generator
def naturalNumbers(n):
    top = n+1
    bottom = 0
    while top > 0 and bottom < n:
        top -= 1
        bottom += 1
        print(top, bottom)

naturalNumbers(5)
#or: 
for i in range(n):
    print(n, n-i-1)
'''
'''
def maclaurin(x, n):
    sum = 0
    term = 1
    denominator = 1
    for i in range(1, n):
        denominator *= i
        term = (x**i)/denominator
        sum += term
    return sum

#print(maclaurin(10, 2))
print(maclaurin(3, 1000))
print(math.exp(3))

# x = "napis"
# x[-1] == od końca, "s"
# x[1:3] == "ap"
# len(x) == 5
# if "a" in x == true
# python strings are immutable
# y = '1.75'
# y.split(".")
'''

#zad 9 

'''
N = 212
n = str(N)
numberCount = len(n)
sum = 0
for i in n:
    sum += int(i)
print(sum)

Collections: 
lists, tuples, dictionaries, sets
x = [1, 2, 3]
len(x) == 3 
x[0] = 2
x.append(4)

Empty list:
x = []

for i in x: 
    print(i)

for i, z in enumerate(x):
    z[i]

list1 = []
for i in range(5):
    list1.append(random.uniform(0, 5))
    print("lista[",i,"]: ", list1[i])
print(len(list1))
print(max(list1), list1.index(max(list1)))
'''

'''
# functions
# global, nonlocal - variable scope
# yield - generator keyword (return-like)
# lambda - anonymous functions
# foo(a=5, b=7) bar(b=7, a=5) valid function calls as long as its defined foo(a, b)
# can also provide default values that way def foo(a, b=3):
# foo(5) => 8
# can be overriden, foo(5, 7) => 12 

def kelvinToCelsius(Tk):
    """docstring"""
    if Tk < 0:
        return None
    Tc = round(Tk - 272.15)
    return Tc


#print(kelvinToCelsius(272.15), "degrees Celsius")

def maclaurin(x, n = 50):
    sum = 0
    term = 1
    denominator = 1
    for i in range(1, n):
        denominator *= i
        term = (x**i)/denominator
        sum += term
    return sum
    
#print(maclaurin(10, 2))
#print(maclaurin(3))
#print(maclaurin(3, 1000))
#print(math.exp(3))


#docstring syntax: """returns x"""

def factorial(n):
    result = 1
    if n == 0 or n == 1:
        return result
    elif n > 1:
        return n * factorial(n-1)
    else:
        return None

print(factorial(20))
print(factorial(-5))
'''

'''
#Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

def fibonacci_iter(n):
    if n == 0:
        second = 0
    else: 
        first = -1
        second = 0
        placeholder = 1
        for i in range(n):
            first = placeholder
            placeholder = second
            second = first + placeholder
    return second

n = []
times = []
for i in range(10):
    start_time = timeit.default_timer()
    fibonacci(n)
    end_time = timeit.default_timer()
    n.append(i)
    times.append(end_time - start_time)
    print("The calculations took", end_time - start_time, "s.")

plt.plot(n, times)

print(fibonacci(10))
print(fibonacci_iter(10))
'''
# Data collections:
# tuple, dict, set
# b = (5, 10, 15)
# b[0] = 7 won't work
# neither will b.append()
# def f():
#   return 2, 6 
# x, y = f()
# b = 1, -> b = (1)
# b = 5, 10, 15
# list comprehension 
# n = [i for i in range(10)] --> n = [0, 1, 2... 10] 
# dont use max or min in hw5 

# no list comprehension for tuples
# but can be converted between each other
# a = [1, 2, 3] 
# b = tuple(a)
# 
# dictionary
# dict comprehension
# d = {i : i*i for i in range(10)}
# del d['i'] <- deletes an element
# iterating over a dict:
# for key, value in d.items():
#   print(key, value)
# for key in d.keys()
# for value in d.values()
# for key in sorted(d.keys()):
# print(key, d[key])
# key has to be immutable, value does not
# if key in dict

'''
arg = [1, 2, 3, 4, 4, 4, 4, 4, 273682]
string1 = "adisfhosfhiofioasshiosahfiasdhasi"
def counter(arg):
    result = {}
    for i in arg:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    for key in sorted(result.keys()):
        print(key, result[key])
    return result

counter(arg)
counter(string1)
'''

# Sets - mutable, but its elements are immutable, nonrepeatable
# Frozenset - same but immutable
# inherently disordered - set[0] doesn't work
# set = {1, 2, 3}
# empty set is not set = {} though, creates a dict
# z1 = set() empty set
# mathematical equivalent of a set 
# sum: z1 | z2, difference z1 - z2, common part z1 & z2, other than z1 ^ z2
# s = {i for i in range(10)}
'''
set1 = {random.randint(5,10) for i in range(20)}
set2 = {random.randint(0,10) for j in range(20)}

print(set1 | set2)
print(set1 - set2)
print(set1 & set2)
print(set1 ^ set2)
'''

# shallow copy
# L1 = [1, 2, 3] 
# L2 = L1[:]  and L2 is L1 
# deep copy
# L2 = L1     and L2 is not L1
# "is" comparator 
# 
#
# lambda funcs
# i.e. sorted(list arg/tuple arg, key (func), reverse (bool))
# 
'''
def sq(x):
    return x*x

sq_lambda = lambda x: x**2

l = [8, -2, 1, 1, 12032193123, 12]

l_sorted = sorted(l, key = lambda x: x**2, reverse = True)
print(l_sorted)'''
'''
people = [('Jan', 'Kowalski'), ('Grzegorz', 'Brzęczyszczykiewicz'), ('Jacek', 'Placek')]

def secondArg(seq):
    return seq[1]

people_sorted = sorted(people, key = secondArg)
print(people_sorted)

people_sorted = sorted(people, key = lambda x: x[1])
print(people_sorted)
'''
'''
# map, filter, reduce
def exec_time(func, *args):
    start = timeit.default_timer()
    func(*args)
    end = timeit.default_timer()
    return end - start

def sq(x):
    return x**2

print(exec_time(sq, 2))
'''

# in/out
# file = open('data.text', use mode ('r (read), w (write, overwrites 
# if already exists), a (append, if exists, appends to the end), b (binary)'))
# file.close() not recommended
# with open('data.txt', 'a') as file: 
# context manager
# file.write(string + '\n')
# file.write(string2) 
# os.mkdir(path), os.path.exists(path) - boolean, os.getcwd() - returns current path
'''
def naturalNumber():
    number = 1
    current = os.getcwd()
    if not os.path.exists(current + '/naturalNumber'):
        os.mkdir(current + '/naturalNumber')
    with open('naturalNumber/even.txt', 'a') as even, open('naturalNumber/odd.txt', 'a') as odd:
        while True:
            number = int(input("Please provide a natural number:"))
            if number == 0:
                break
            elif number % 2 == 0:
                even.write(str(number) + '\n')
            elif number % 2 == 1:
                odd.write(str(number) + '\n')
naturalNumber()
'''
# os.listdir() - ls 

# with open('naturalNumber/even.txt', 'r') as even:
#   evenContent = even.read()
#   lines = even.read().splitlines()
#   lines2 = []
#   for line in even.readlines():
#       lines2.append(line) 

'''
def readNumbers():
    evenLines = []
    oddLines = []
    with open('naturalNumber/even.txt', 'r') as even:
        counter = 0
        evenSum = 0
        evenMean = 0
        for evenLine in even.readlines():
            counter += 1
            evenSum += int(evenLine)
            evenLines.append(int(evenLine))
        evenMean = evenSum / counter
    with open('naturalNumber/odd.txt', 'r') as odd:
        counter = 0
        oddSum = 0
        oddMean = 0
        for oddLine in odd.readlines():
            counter += 1
            oddSum += int(oddLine)
            oddLines.append(int(oddLine))
        oddMean = oddSum / counter
    return evenSum, evenMean, oddSum, oddMean

print(readNumbers())
'''
'''
from matplotlib.animation import FuncAnimation
M = np.zeros((6,6))
M[2,2] = 1
M[2,3] = 1
M[2,4] = 1
M[3,1] = 1
M[3,2] = 1
M[3,3] = 1
matrices = []
T = 30 #number of iterations

for k in range(T): 
  M_next = M.copy()
  plt.imshow(M_next)
  plt.show()
  for i in range(1, 5):
    for j in range(1, 5):
      sub_M = M[i-1:i+2, j-1:j+2]
      sum1 = np.sum(sub_M) - M[i,j]
      if M[i,j] == 1:
        if sum1 > 3 or sum1 < 2:
          M_next[i,j] = 0
        M = M_next.copy()
      else:
        if sum1 == 3:
          M_next[i,j] = 1
        M = M_next.copy()
'''
'''
class Kot: # nazywamy z duzej litery
    def __init__(self, name): #konstruktor
        self.name = name  # atrybut
        print("tworzymy kota")
    def miau(self): # metoda
        print("Miau, tu {}!".format(self.name))
    

kot = Kot("Filemon") # tutaj się wywołuje konstruktor
kot2 = Kot("Jurek")
kot.miau()
print(kot.name)
kot.name = "Stefek"
kot.miau()
print(type(kot))
'''
'''
# exceptions
try: 1/0
except ZeroDivisionError:
    print("xd.")
else: 
    # execute if no exception present 
    pass
finally:
    # execute regardless
    pass
'''

class EmptyListError(Exception):
    pass

list1 = [1, 2, 827272, 3, 99, 101]
list2 = []


def switch(collection, i, j):
    '''Fill in what the function does and exceptions it can raise'''
    if len(collection) == 0:
        raise EmptyListError
    try:
        collection[i], collection[j] = collection[j], collection[i]
    except Exception:
        raise

try:
    switch(list1, 0, 1)
    print(list1)
except EmptyListError:
    print("Empty list.")