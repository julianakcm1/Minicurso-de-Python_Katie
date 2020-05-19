print("Digite a nota 1: ")
nota1 = float(input())

print("Digite a nota 2: ")
nota2 = float(input())

print("Digite a nota 3: ")
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aluno aprovado!", "Média = {:.3f}".format(media))

elif media < 7 and media >= 5:
    print("Aluno em recuperação.", "Média = {:.3f}".format(media))

else:
    print("Aluno reprovado.", "Média = {:.3f}".format(media))
