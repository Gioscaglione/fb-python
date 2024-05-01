C = int(input("Código: " ))
N = int(input("Horas: " ))

if (N>50):
    salario = 50 * 10 
    HorasExtra = N - 50
    E = HorasExtra * 20
    salarioTotal = salario+E
    print(salario)

else:
    salario = N*10
    print(salario)