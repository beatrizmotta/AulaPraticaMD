# Escrever um programa para listar o maior número possível números primos em 60 
# segundos (sequencialmente)

import time 
 
primos = list()

i = 1

while time.perf_counter() <= 60:    
    for n in range(2, i):
        if (i == n):
            break
        elif (i % n == 0):
            break
        else:
            primos.append(i)
            break
    i = i + 1


print("Foram computados %d números primos." % len(primos))
print("Último número primo da lista: %d" % primos[len(primos)-1])
quit()
    