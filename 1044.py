values = input().split()
a = int(values[0])
b = int(values[1])

if b % a == 0 or a % b == 0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")