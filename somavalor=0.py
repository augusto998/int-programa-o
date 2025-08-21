somavalor=0
contnegativa=0
for i in range (20):
    valor=int(input("digite o valor:"))
    if valor >0:
        somavalor=somavalor+valor
    else:
        contnegativa=contnegativa+1
print("a soma dos valores positivos é",somavalor)
print("a quantidade dos valores negativos é",contnegativa)
