def insertion_sort(lista):
    for i in range(1, len(lista)):
        termo = lista[i]
        j = i
        while j > 0 and termo < lista[j-1]:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = termo

    return lista

