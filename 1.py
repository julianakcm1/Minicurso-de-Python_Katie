#print("Digite o peso:")
peso = float(input("Digite o peso:\n"))
#print("Digite a altura:")
altura = float(input("Digite a altura:\n"))

imc = peso / (altura*altura)

print("IMC = {:.4f}".format(imc))
