# Escrever um programa para determinar o mdc de dois números com base no Al-
# goritmo de Euclides.

import math

def euclides(num1, num2, p1, p2):
    if (num1 == num2):
        mdc = num1
    elif (num1 > num2):
        a = num1
        d = num2
    elif (num1 < num2):
        a = num2
        d = num1 
    
    q = math.floor(a / d)
    r = a % d

    if (r == 0):
        mdc = d
        print("%d = %d * %d + %d" % (a, q, d, r))
        print("O MDC de (%d, %d) é %d" % (p1, p2, mdc))
    else:
        print("%d = %d * %d + %d" % (a, q, d, r))
        aux = d
        a = aux
        d = r
        euclides(a, d, p1, p2)  
    


    
numbers = input("Digite dois números inteiros (separados por espaço): ")
numbers = numbers.split(' ')

num1 = int(numbers[0])
num2 = int(numbers[1])

results = euclides(num1, num2, num1, num2)
print(results)