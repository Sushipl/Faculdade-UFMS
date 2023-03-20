print("Organizando em ordem crescente")
num1 = int(input("Primeiro número da lista: "))
num2 = int(input("Segundo número da lista: "))
num3 = int(input("Terceito número da lista: "))
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
if num2 > num3:
    temp = num2
    num2 = num3
    num3 = temp
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
print(num1, num2, num3)