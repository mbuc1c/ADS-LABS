from code import *

object1 = Randomier()
object2 = Randomier()

print(object1.__repr__())
print(object2.__repr__())

print("Checking equality of the two different objects with defined ids':")
print(f"OB with id:{object1.__str__()} == OB with id:{object2.__str__()}")
print(object1.__eq__(object2))
print("Checking equality to itself: ")
print(object1.__eq__(object1))