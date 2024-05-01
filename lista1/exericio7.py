a = int(input("Digite o número a: "))
b = int(input("Digite o número b: "))
c = int(input("Digite o número c: "))
d = int(input("Digite o número d: "))
e = int(input("Digite o número e: "))
f = int(input("Digite o número f: "))

x = (c * e - (b * f)) / (a * e - (b * d))
y = (a * f - (c * d)) / (a * e - (b * d))

print(f"O valor de y é: {y}")
print(f"O valor de y é: {x}")