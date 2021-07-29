def primeiro_lex(lista):
    min = lista[0]
    for i in range(len(lista)-1):
        if min > lista[i+1]:
            min = lista[i+1]
    return min


lista = ['oĺá', 'A', 'a', 'casa']
print(primeiro_lex(lista))