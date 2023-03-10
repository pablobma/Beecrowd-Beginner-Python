values = input().split()
A = int(values[0])
B = int(values[1])
C = int(values[2])
D = int(values[3])

if B>C and D>A and C+D>A+B and C>0 and D>0 and A>0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
