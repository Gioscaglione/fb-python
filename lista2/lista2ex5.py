indice = float(input("Digite o indice: "))

if (indice<0.3 and indice>=0):
    print("O índice de poluição está dentro do esperado")
elif(indice >= 0.3 and indice <0.4):
    print("O índice de poluição está alto, fechamento primeiro grupo")
elif(indice >= 0.4 and indice < 0.5):
    print("O índice de poluição está alto, causando o fechamento do primeiro e segundo grupo")
elif(indice >= 0.5):
    print("O índice de poluição está alto, fechamento de todos os grupos)")
else:
      print("Escreva um número aceitável")


