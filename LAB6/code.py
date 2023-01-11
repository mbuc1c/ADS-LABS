# LAB - 06 2021

def string_to_ascii_sort():
    inpt = input("Please enter a sentence here: \n")
    lst = inpt.split()

    print("Ulazna lista: " + str(lst))
    ascii_lst = []
    for word in lst:
        ascii_lst.append(sum(map(ord, word)))

    print("Lista s ekvivalentim ascii vrijednostima: ")
    print(ascii_lst)
    print("Sortirana uzlazno: ")
    print(sorted(ascii_lst))
    print("Sortirana silazno: ")
    print(sorted(ascii_lst, reverse=True))