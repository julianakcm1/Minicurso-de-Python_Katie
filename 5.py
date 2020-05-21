#sem usar a math
def hipotenusa(cat_oposto, cat_adjacente):
    hipotenusa = (cat_oposto**2 + cat_adjacente**2) ** (1/2)
    return hipotenusa

cat_oposto = float(input("Digite o cateto oposto: "))
cat_adjacente = float(input("Digite o cateto adjacente: "))

resultado = hipotenusa(cat_oposto, cat_adjacente)
print("O valor da hipotenusa é: {}".format(resultado))
