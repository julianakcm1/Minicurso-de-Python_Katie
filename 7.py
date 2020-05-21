#print("Digite uma lista de números:")
lista = (input("Digite uma lista de números:\n")).split()
"""
maior = -99999
menor = 99999
soma  = 0

for i in range(len(lista)):
    lista[i] = int(lista[i]) #Cast

    if lista[i] > maior:
        maior = lista[i]

    if lista[i] < menor:
        menor = lista[i]

    soma += lista[i]

    print("Maior =", maior, "Menor =", menor, "Soma =", soma)
"""
lista2 = []

for i in range(len(lista)):
    lista2.append(int(lista[i]))

print("Maior = ", max(lista2), ". Menor = ", min(lista2), ". Soma = ", sum(lista2), ".")
