# LAB - 02 2021

def get_even(*args):
    lista = []
    lista.extend(args)
    evenList = []
    for element in lista:
        if element % 2 == 0:
            evenList.append(element)

    return (evenList, lista)


def get_odd(lista):
    oddList = []
    for element in lista:
        if element % 2 != 0:
            oddList.append(element)

    return oddList