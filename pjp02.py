arq = open("VENDAS.txt", "r")  
s = arq.readline()
lista = []

while s != "":   # Algoritmo para ler os dados do programa
    s = s.rstrip()
    item = s.split(";")
    total = float(item[1]) * float(item[2])
    lista.append(item[0])
    lista.append(float(item[1]))
    s = arq.readline()     
arq.close()

while True:  # Entrada do código do produto e saída do programa
    entrada = str(input("Digite o código do produto: "))
    if int(entrada) == 0:
        print("Fim do programa.")
        break
    elif entrada in lista:  # Soma do total do produto digitado
        for i in range(len(lista)-1):
            soma = lista[i+1]
            for j in range(len(lista)-1):
                if lista[i] == lista[j] and i != j:
                    soma = soma + lista[j+1]
        print("Total vendido do produto {} = R$ {:.2f}".format(entrada, soma))
    elif int(entrada) < 10000 or int(entrada) > 21000:  # Valores inválidos
        print("Entrada inválida. Digite o número do código entre 10.000 e 21.000")
    else:  # Código do produto que não estiver no documento
        print("Total vendido do produto {} = R$ 0.00".format(entrada))
    

    
