numero = int(input("Digite um número positivo: "))
if numero < 0 :
    print("Vc digitou um negativo")
elif numero == 0:
    print ("Vc digitou o zero, zero é neutro")
elif (numero % 2 == 0):
    print("O número é par")
else:
    print("O número é impar")

print("Fim do programa")