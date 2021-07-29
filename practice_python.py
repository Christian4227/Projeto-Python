# Quadro de empregos

def lista_empregos():
    print("------------------------------------------------")
    lista = ["Administração", "Direito", "Educação Física", "Fisioterapia", "Farmácia", "Química", "Medicina",
             "Veterinária"]
    for i in range(len(lista)):
        print(lista[i])


print("------------ Site de empregos Cubo ------------")

# Preenchimento dos dados pessoais do candidato
nome = input("Digite o seu nome: ")
idade = int(input("Idade: "))
data_nascimento = input("Data de nascimento: ")
lista_empregos()
area_profissional = input("Profissão: ")

# Função para validar o gênero e imprimir por extenso de acordo com a entrada
while True:
    genero = input("Gênero: Masculino (M); Feminino (F); Não binário (B) ")
    if genero == "M" or genero == "F" or genero == "B":
        if genero == "M":
            genero = "Masculino"
            break
        elif genero == "F":
            genero = "Feminino"
            break
        else:
            genero = "Não binário"
            break
    else:
        print("Entrada inválida. Digite M, F ou B ")

# Formulário para mostrar os dados para o cliente
print("-"*50)
print("Nome: {:25} Idade: {} anos\nSexo: {:25} Data de nascimento: {}".format(nome, idade, genero, data_nascimento))
print("Profissão: {:30}".format(area_profissional))
