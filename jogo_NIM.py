### JOGO DO NIM ###

def player_joga(n, m):
    pecas = int(input("Digite o número de peças que você quer retirar. "))
    if pecas > m or pecas > n or pecas == 0:
        print("Jogada inválida. Tente novamente.")
        return player_joga(n, m)
    else:
        return pecas

def computador_joga(n, m):
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        else:
            return m



def partida():
    n = int(input("Digite o número inicial de peças: "))
    m = int(input("Digite o número máximo de peças que podem ser retiradas: "))

    cpu = 0
    if n % (m+1) == 0:
        print("O jogador começa!")
        cpu = 0
    else:
        print("O computador vai começar!")
        cpu = 1

    computador = False
    jogador = False
    while n > 0:
        if cpu == 1:
            a = computador_joga(n, m)
            print("O computador retirou {} peças".format(a))
            n -= a
            computador = True
            jogador = False
        else:
            a = player_joga(n, m)
            print("Você retirou {} peças".format(a))
            n -= a
            jogador = True
            computador = False
            cpu = 0
        print("Peças restantes: {} peças no tabuleiro".format(n))
        cpu += 1

    if jogador:
        print("Parabéns! Você venceu!")
        return 1
    else:
        print("Mais sorte da próxima vez. O computador venceu!")
        return 0


def jogo_completo():
    i = 1
    jogador = 0
    computador = 0

    while i <= 3:
        a = partida()
        if a == 1:
            jogador += 1
        else:
            computador += 1
        i += 1

    if jogador > computador:
        print("Você venceu o campeonato! Parabéns!")
    else:
        print("Não foi dessa vez. O computador venceu.")


def main():
    print("Escolha a sua opção: 1- partida simples; 2- Jogo completo")
    escolha = int(input("Escolha: "))
    if escolha == 1:
        partida()
    elif escolha == 2:
        jogo_completo()
    else:
        print("Entrada inválida. Digite novamente.")
        print("-"*50)
        main()


print("-"*50)
print("-"*50)
print("Bem vindo ao Jogo do NIM!!!!".center(40))
print("-"*50)
print("-"*50)
main()
