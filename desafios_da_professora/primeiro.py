print("Organizando em ordem crescente")
num1 = int(input("\033[1mPrimeiro número da lista: "))
num2 = int(input("\033[1mSegundo número da lista: "))
num3 = int(input("\033[1mTerceito número da lista: "))
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3 ,num2
if num1 > num2:
    num1, num2 = num2, num1
print("\033[32m", num1, num2, num3, "\033[0m")