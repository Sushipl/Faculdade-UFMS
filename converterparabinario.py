num = int(input())
p = []
while num > 0:
    p.append(num%2) 
    num = num//2
print(p)
