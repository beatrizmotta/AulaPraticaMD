#Decompõe um inteiro em fatores primos

number = input('Digite um número inteiro: ')
number = int(number)

#Encontrar os divisores
divisores = list() 
for k in range(2, number):
    if (number % k == 0):
        divisores.append(k)

#Encontrando os fatores primos entre os divisores
divisores_primos = list()
for l in divisores:
    primo = True
    for i in range(2, l):
        if (l % i == 0):
            primo = False
    
    if (primo):
        divisores_primos.append(l)

print("Divisores:")
print(divisores)
print("Divisores Primos:")
print(divisores_primos)

fatores = list()

index = 0

newN = number

while (index < len(divisores_primos)):
    # print("%d / %d = %d" % (number, divisores_primos[index], (number / divisores_primos[index])))
    if ((newN / divisores_primos[index]) % divisores_primos[index] == 0):
        fatores.append(divisores_primos[index])
        newN = newN / divisores_primos[index]
        continue
    else:
        fatores.append(divisores_primos[index])
        newN = newN / divisores_primos[index]
        index = index + 1
        continue

fatores_str = list()
for m in fatores:
    fatores_str.append(str(m))

print("%d pode ser decomposto em:" % number)
print(" * ".join(fatores_str))










