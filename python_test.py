import time
import random

# def grupo_testes():
    # @pytest

def grupo_dados():
    a = 3
    b = 5
    c = 4
    d = 9
    antes = time.time()
    soma = 0
    for i in range(10):
        soma = soma + random.randint(0, 100)
    depois = time.time()
    print(depois - antes)

grupo_dados()