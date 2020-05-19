print("Digite uma lista de números:")
lista = input().split()

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
