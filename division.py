import timeit

num1, num2 = 2, 3
start = timeit.default_timer()

try:
    result = num1 / num2
except ZeroDivisionError:
    pass
else:
    print(result)
finally:
    end = timeit.default_timer()
    print("The time was", end - start)
