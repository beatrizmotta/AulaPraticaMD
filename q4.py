# Escrever um programa para determinar o mdc e o mmc de dois inteiros com base
# em seus fatores primos.

numbers = input('Digite os dois inteiros (separados por um espaço): ')
numbers = numbers.split(' ')

number1 = int(numbers[0])
number2 = int(numbers[1])

# Para o primeiro número
divisores1 = list() 
for k in range(2, number1):
    if (number1 % k == 0):
        divisores1.append(k)


divisores1_primos = list()
for l in divisores1:
    primo = True
    for i in range(2, l):
        if (l % i == 0):
            primo = False
    
    if (primo):
        divisores1_primos.append(l)

fatores1 = list()
index1 = 0
newN1 = number1

while (index1 < len(divisores1_primos)):
    if ((newN1 / divisores1_primos[index1]) % divisores1_primos[index1] == 0):
        fatores1.append(divisores1_primos[index1])
        newN1 = newN1 / divisores1_primos[index1]
        continue
    else:
        fatores1.append(divisores1_primos[index1])
        newN1 = newN1 / divisores1_primos[index1]
        index1 = index1 + 1
        continue


# Para o segundo número
divisores2 = list() 
for k in range(2, number2):
    if (number2 % k == 0):
        divisores2.append(k)


divisores2_primos = list()
for l in divisores2:
    primo = True
    for i in range(2, l):
        if (l % i == 0):
            primo = False
    
    if (primo):
        divisores2_primos.append(l)

fatores2 = list()
index2 = 0
newN2 = number2

while (index2 < len(divisores2_primos)):
    if ((newN2 / divisores2_primos[index2]) % divisores2_primos[index2] == 0):
        fatores2.append(divisores2_primos[index2])
        newN2 = newN2 / divisores2_primos[index2]
        continue
    else:
        fatores2.append(divisores2_primos[index2])
        newN2 = newN2 / divisores2_primos[index2]
        index2 = index2 + 1
        continue

mdc = 1
mmc = 1

new_elements_f_1 = dict()
new_elements_f_2 = dict()

# Se um dos números for primo
if (fatores1.__len__ == 0 or fatores2.__len__ == 0):
    mdc = 1
    mmc = 1
else:
    for n in fatores1:
        if (n in new_elements_f_1):
            new_elements_f_1[n] = new_elements_f_1[n] + 1
        else:
            new_elements_f_1[n] = 1
    for n in fatores2:
        if (n in new_elements_f_2):
            new_elements_f_2[n] = new_elements_f_2[n] + 1
        else:
            new_elements_f_2[n] = 1

    for n in new_elements_f_1:
        if (n not in new_elements_f_2):
            new_elements_f_2[n] = 0
    for n in new_elements_f_2:
        if (n not in new_elements_f_1):
            new_elements_f_1[n] = 0

    fatoracaoMDC = list()
    fatoracaoMMC = list() 

    print(new_elements_f_1)
    print(new_elements_f_2)

    for l in new_elements_f_1:
        if (new_elements_f_1[l] >= new_elements_f_2[l]):
            fatoracaoMMC.append([l, new_elements_f_1[l]])
        elif (new_elements_f_2[l] >= new_elements_f_1[l]):
            fatoracaoMMC.append([l, new_elements_f_2[l]])

    for l in new_elements_f_1:
        if (new_elements_f_1[l] <= new_elements_f_2[l]):
            fatoracaoMDC.append([l, new_elements_f_1[l]])
        elif (new_elements_f_2[l] <= new_elements_f_1[l]):
            fatoracaoMDC.append([l, new_elements_f_2[l]])

    for m in fatoracaoMDC:
        mdc = mdc * m[0] ** m[1]
    
    for m in fatoracaoMMC:
        mmc = mmc * m[0] ** m[1]

print("O MDC de %d e %d: é %d" % (number1, number2, mdc))
print("O MMC de %d e %d: é %d" % (number1, number2, mmc))











    # for n in fatores1:
    #     if (n not in fatores2):
    #         new_element_f_2.append([n, 0])
    # for n in fatores2:
    #     if (n not in fatores1):
    #         new_elements_f_1.append([n, 0])



# Definindo quantas vezes cada fator se repete 





