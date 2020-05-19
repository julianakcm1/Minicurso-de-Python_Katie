def function (espaco, tempo, velocidade):
    velocidade_media = espaco/tempo
    aceleracao = velocidade_media/tempo
    print("Velocidade média = {:.5f}".format(velocidade_media))
    print("Aceleração = {:.5f}".format(aceleracao))

print("Digite o espaço (em metros): ")
espaco = float(input())

print("Digite o tempo (em segundos): ")
tempo = float(input())

print("Digite a velocidade (em metros/segundo): ")
velocidade = float(input())

function(espaco, tempo, velocidade)
