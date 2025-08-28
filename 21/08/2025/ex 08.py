thanos= 150 
homem_aranha=110
a = 100
contagem=0
for i in range (a):
    thanos+=0.02
    homem_aranha+=0.03
    contagem +=1
    if homem_aranha > thanos:
        print("agora homem aranha é maior que thanos e levou:",contagem,"anos pra ser maior")
        break
