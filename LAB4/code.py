import random as r

def randomList(size):
    lista = []
    for i in range(size):
        lista.append(r.randint(0, size))

    return lista


def duplicates(list):
    uniceElementList = []
    duplicatesList = []
    for element in list:
        if element not in uniceElementList:
            uniceElementList.append(element)
        else:
            duplicatesList.append(element)
    return sorted(uniceElementList), sorted(duplicatesList)
