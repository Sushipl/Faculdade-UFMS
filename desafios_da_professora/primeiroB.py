list = []
print("Dígite números inteiros para a lista de 3 números")
while len(list) != 3:
    pos = ['primeira', 'segunda', 'terceira']
    try: 
        nnum = int(input("Dígite um número inteiro para {} posição: ".format(pos[len(list)])))
        list.append(nnum)
    except:
        print("Dígite corretamente!")
list.sort(key=int)
for ele in list:
    print(ele, end=" ")