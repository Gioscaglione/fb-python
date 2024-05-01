dias_totais = int(input("Digite sua idade em dias: "))
anos = dias_totais // 365
meses = (dias_totais % 365) // 30
dias = ((dias_totais % 365)) % 30

print (f"Anos: {anos}\n Dias: {dias}\n Meses: {meses}")