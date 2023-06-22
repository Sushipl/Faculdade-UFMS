def determineSeOrdenado(list = []):
    res = 1
    le = len(list)
    cont = 0
    while cont < le-1 and res == 1:
        print(f"{le-2} a {cont}")
        if list[cont] > list[cont+1]:
            res = 0
        cont+=1
    return res
lis = []
n = int(input("tamanho da lista"))
while n < 0 or n > 40:
    n = int(input("tamanho da lista"))
for nu in range(n):
    lis.append(int(input()))

print(determineSeOrdenado(lis))