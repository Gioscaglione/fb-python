P = int(input("Digite o peso: "))

E = 0
M = 0

if(P>50):
    E = P - 50
    M = (E*4)
    print(f"O valor da multa será {M}")
else:
    print("Sem multa")