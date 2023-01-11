from code import *

# lista = randomList(11)
# listaSorted = duplicates(lista)
#
# print(lista)
# print(listaSorted)


lst = input("enter a list elements: ")
lst = lst.split(", ") # use split
lst = list(map(int,lst)) # do not change -> see map. filter, reduce
print("List: ")
print(lst)
unique, duplicates = duplicates(lst)
print("Unique:")
print(unique)
print("Duplicates: ")
print(duplicates)
