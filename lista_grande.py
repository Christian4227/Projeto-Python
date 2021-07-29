import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randrange(n))
    return lista


print(lista_grande(6))