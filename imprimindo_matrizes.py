def imprime_matriz(matriz):
    linhas = len(matriz)
    coluna = len(matriz[0])
    print("linhas =", linhas)
    print("Colunas =", coluna)

    for i in range(linhas):
        for j in range(coluna):
            print("{}".format(matriz[i][j]), end="")
            if j != coluna-1:
                print(end=" ")
            else:
                print(end="")
        if i != linhas-1:
            print(end="")
            print("")
    print("")


matriz_2 = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
matriz = [[1], [2]]
imprime_matriz(matriz_2)