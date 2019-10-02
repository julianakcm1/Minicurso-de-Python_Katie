nota1 = float (input ())
nota2 = float (input ())
nota3 = float (input ())
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print (media,'\n',"Aprovado!")
elif media >= 5 and media < 7:
    print (media,'\n',"Recuperação!")
else:
    print (media,'\n',"Reprovado!")