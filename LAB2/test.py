import code

tupleVar = code.get_even(21, 3, 4, 8, 9, 14, 16, 78, 101)

print("Even from input args: " + str(tupleVar[0]))

od = code.get_odd(tupleVar[1])

print("Odd elements from input: " + str(od))