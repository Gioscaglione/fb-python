valor = float(input("Digite o valor a custo de fábrica: "))

per_dist = valor * 0.28
imp = valor * 0.45

total = valor + per_dist + imp

print(f"O valor ao custo consumidor é de {total}")