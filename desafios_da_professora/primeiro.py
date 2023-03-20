print("Organizando em ordem crescente")
num1 = int(input("Primeiro número da lista: "))
num2 = int(input("Segundo número da lista: "))
num3 = int(input("Terceito número da lista: "))
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3 ,num2
if num1 > num2:
    num1, num2 = num2, num1
print(num1, num2, num3)