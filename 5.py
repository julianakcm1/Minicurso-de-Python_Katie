def function (espaco, tempo):
    velocidade_media = espaco/tempo
    aceleracao = velocidade_media/tempo
    print("Velocidade média = {:.5f}".format(velocidade_media))
    print("Aceleração = {:.5f}".format(aceleracao))

#print("Digite o espaço (em metros): ")
espaco = float(input("Digite o espaço (em metros): "))

#print("Digite o tempo (em segundos): ")
tempo = float(input("Digite o tempo (em segundos): "))

function(espaco, tempo)
