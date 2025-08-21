#4
somaAltura=0
nvolei=int(input("digite o numero de  jogadores:"))
for i in range (0,nvolei):
    altura=float(input("digite a altura dos jogadores:"))
    somaAltura+=altura
soma=somaAltura/nvolei
print("a media da altura dos jogadores é:",soma)

