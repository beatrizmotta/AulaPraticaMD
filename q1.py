## Escrever um programa que determina se um dado número inteiro é primo ou não. ## 

number = input("Digite um número inteiro:\n")
number = int(number)

i = 1
divisores = list()

#Descobre os divisores de n
while (i <= number):
    if (number % i == 0):
        divisores.append(i)
    i = i + 1

#Conta quantos divisores diferentes de 1 e n, n tem 
divisores_compostos = 0
for j in divisores:
    if (j != 1 and j != number):
        divisores_compostos = divisores_compostos + 1

#Se esse número for maior ou igual a um, isso quer dizer que o número é composto. Caso não, é primo.
if (divisores_compostos >= 1):
    print("%d é um número composto.\nSeus divisores são:" % number)
    print(divisores)
elif (divisores_compostos == 0):
    print("%d é um número primo.\nSeus divisores são:" % number)
    print(divisores)




