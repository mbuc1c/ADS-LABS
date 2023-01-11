# LAB - 01 2021

def miniMaxi(*numbers):
    lista = []
    lista.extend(numbers)
    mini = lista[0]
    maxi = lista[0]
    for element in lista:
        if element > maxi:
            maxi = element
        elif element < mini:
            mini = element
    return lista, (mini, maxi)

print(miniMaxi(23, 4, 55, 11, 2, 3, 56, 789, 0, 123))
