lista = [1,2,3,4,5,6,7,8,9,10]

def busquedalineal(x, lista):

    index = 0

    for i in lista:
        if i == x:
            return index
        
        index = index + 1

    return -1


print(busquedalineal(5,lista))