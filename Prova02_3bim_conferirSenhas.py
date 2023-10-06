#Júlio César Diniz, 2º Informática
#Prova 02 do 3° Bimestre - 05/10/2023 - Laboratório de Linguagem de Programação  II

senhas = []
conferesenhas = []
especiais = ['!', '@', '#', '$', '%', '&', '*', '_']
print("Por favor, insira 4 senhas: ")
print("As senhas devem conter pelo menos 8 caracteres, contendo pelo menos uma letra maiúscula e uma minúscula, um número e um caractere especial.")
for i in range(4):
    print("senha " + str(i + 1))
    senha = input()
    senhas.append(senha)

    for senha in senhas:
        maiuscula = False
        minuscula = False
        alnum = False
        especial = False

    if (len(senha) >= 8):
        for char in senha:
            if (char.isupper()):
                maiuscula = True
            elif (char.islower()):
                minuscula = True
            elif (char.isalnum()):
                alnum = True
            elif char in especiais:
                especial = True;

    conferesenhas.append(maiuscula and minuscula and alnum and especial)
print(senhas)
print(conferesenhas)
