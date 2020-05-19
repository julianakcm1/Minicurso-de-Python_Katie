i = 1
while i < 200:
    if i % 2 == 0:
        print(i)
    i += 1

quantidade_de_pares = 0
for i in range (200):
    if i % 2 == 0:
        quantidade_de_pares += 1

print("Quantidade de números pares entre 0 e 200 =", quantidade_de_pares)
