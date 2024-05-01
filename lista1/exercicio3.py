seg = int(input("Digite o tempo em segundos: "))
horas = seg//3600
min = (seg%3600)//60
segundos = (seg%3600)%60

print(f"Segundos: {segundos}\nHoras: {horas}\nMinutos: {min}")
