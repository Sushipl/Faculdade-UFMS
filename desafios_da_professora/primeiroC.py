from num2words import num2words

list = []
print("Dígite números inteiros para a lista, ela será organizada em ordem crescente (dígite 'pare' para parar a listagem)")
while True:
    try: 
        nnum = input("Dígite um número inteiro para o {} lugar: ".format(num2words(len(list)+1, lang="pt-br", to="ordinal")))
        if nnum == 'pare':
            break
        list.append(int(nnum))
    except:
        print("Dígite corretamente!")
list.sort(key=int)
print("Você digitou {} números".format(len(list)))
for ele in list:
    print(ele, end=" ")