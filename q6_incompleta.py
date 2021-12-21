# Escrever um programa para encontrar os coeficientes s e t da combinação linear
# mdc(a, b) = s · a + t · b.

import math

def combicaolinear(num1, num2, array):
    arr = array
    if (num1 > num2):
        a = num1
        d = num2
    elif (num1 < num2):
        a = num2
        d = num1 

    q = math.floor(a / d)
    r = a % d 

    if (r == 0):
        arr.append([a, q, d, r])
        return arr
    else:
        arr.append([a, q, d, r])
        aux = d 
        a = aux
        d = r
        return combicaolinear(a, d, arr)

numbers = input("Digite dois números inteiros (separados por espaço): ")
numbers = numbers.split(' ')

num1 = int(numbers[0])
num2 = int(numbers[1])

arr = list()
results = combicaolinear(num1, num2, arr)
results.reverse()

mdc = results[0][3]

for i in results:
    print("%d = %d * %d + %d" % (i[0], i[1], i[2], i[3]))

# for i in range(0, len(results)):
#     if (results[i][0] == mdc):
#         print(results[i])
#         if (i == len(results)-1):
#             print("Pronto para resolver a combinaçao")
#         else:
#             print("Esta expressão está na posição %d de %d." % (i, len(results)-1))
        