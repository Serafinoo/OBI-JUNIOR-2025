# m = limite de calorias, n =  gorduras e carboidratos nas refeições
#1 grama de proteina = 4 calorias
#1 grama de gordura = 9 calorias
#1 grama de carboidrato = 4 calorias
lista = []
n,m = [int(i) for i in input().split()]
for n in range (n):
    p,g,c = [int(j) for j in input().split()]
    cal = p * 4 + g * 9 + c * 4
    lista.append(cal)
    tot_cal = (sum(lista))
    quanto_cal = m - tot_cal
print(quanto_cal)