from random import randint

def gerar_senha(tipo, tam):  # Função para o usuário criar a senha antes de ler o documento MATR.txt
    senha = ""
    if tipo == 'a':  # Condição para gerar senha do tipo Numérica
        for i in range(tam):
            s = randint(48, 57)
            senha = senha + chr(s)
        return senha
    elif tipo == 'b':  # Condição para gerar o tipo de senha Numérica
        for i in range(tam):
            if i % 2 == 0:
                s = randint(65, 90)
            else:
                s = randint(97, 122)
            senha = senha + chr(s)
        return senha
    elif tipo == 'c':
        for i in range(tam-1):
            if i % 2 == 0:
                s = randint(48, 57)
            else:
                s = randint(65, 90)
            senha = senha + chr(s)
        return senha
    elif tipo == 'd':
        for i in range(tam):
            if i % 3 == 0:
                s = randint(48, 57)
            elif i % 3 == 1:
                s = randint(65, 90)
            else:
                s = randint(95, 122)
            senha = senha + chr(s)
        return senha
    elif tipo == 'e':
        for i in range(tam):
            if i % 4 == 0:
                s = randint(33, 46)
            elif i % 4 == 1:
                s = randint(48, 57)
            elif i % 4 == 2:
                s = randint(58, 90)
            else:
                s = randint(97, 122)
            senha = senha + chr(s)
        return senha


arquivo = open("MATR.txt", "r")  # Arquivo para ler MATR.txt
arquivo_2 = open("SENHAS.txt", "w")  # Arquivo para escrever SENHAS.txt
tipo = input("Digite o tipo de senha que você deseja gerar: ")
tam = int(input("Quantidade de caracteres para a sua senha: "))
s = arquivo.readline()
while s!= "":  # Looping para ler as linhas do arquivo MART.txt
    senha = gerar_senha(tipo, tam)  # Função para gerar a senha
    s = s.rstrip()
    linha = "{};{}".format(s, senha)  # Formato para imprimir a linha com a senha e a matrícula junto
    arquivo_2.write(linha + "\n") 
    s = arquivo.readline()
arquivo_2.close()
arquivo.close()

