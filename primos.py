def n_primos(n):
    i = 3
    primos = 1

    if n == 2:
        return 1
    while i <= n:
        s = 2
        e_primo = True
        while s < i:
            if i % s == 0:
                e_primo = False
                break
            s += 1
        print(e_primo)
        if e_primo:
            primos += 1
        i += 1
    return primos

