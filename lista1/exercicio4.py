import math

a = int(input("Digite o número A: "))
b = int(input("Digite o número B: "))
c = int(input("Digite o número C: "))

r = math.pow(a+b,2)
s = math.pow(b+c,2)

d = (r+s)/2

print(d)