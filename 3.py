#print("Digite os segundos:")
segundos = float(input("Digite a quantidade de segundos:\n"))

horas    = segundos // 3600
segundos = segundos % 3600 #pegar o resto
minutos  = segundos // 60
segundos = segundos % 60

#horas = minutos / 60

#print(horas, "hora(s)", minutos, "minuto(s)", segundos, "segundo(s)")
print("{}h {}min {}s".format(horas, minutos, segundos))
