tot = []

camp = input("Nome do aluno: ").upper()

while camp != "FIM":
    tot.append(camp)
    for n in range(1, 4):
        j = int(input(f"{n}ª nota do aluno: "))
        while j <= 0 or j > 10:
            j = int(input(f"{n}ª nota do aluno: "))
        tot.append(j)
    camp = input("Nome do aluno: ").upper()

print("-"*30)
for op in range(0, len(tot), 4):
    med = (tot[op+1]+tot[op+2]+tot[op+3])/3
    print(f"{tot[op]:10} {med:5.2f} {'aprovado' if med >= 6 else 'reprovado':10}")
print("-"*30)