print("Digite os segundos:")
segundos = int(input())

horas    = segundos // 3600
segundos = segundos % 3600 #pegar o resto
minutos  = segundos // 60
segundos = segundos % 60

#horas = minutos / 60

print(horas, "hora(s)", minutos, "minuto(s)", segundos, "segundo(s)")

#segundos em float
#print("{:.3f}h".format(horas), minutos, "min", segundos, "s")
