def e_hipotenusa(n):

    for i in range(1, n):
        for j in range(1, n-1):
            eq = n ** 2 == i ** 2 + j ** 2
            if eq:
                return True

    return False

def soma_hipotenusas(n):
    m = 1
    soma = 0

    while m <= n:
        print(m)
        if e_hipotenusa(m):
            soma += m
        m += 1

    return soma