values = input().split()
a = int(values[0])
b = int(values[1])
c = int(values[2])

if a>=b and a>=c:
    greatest = a
elif b>=a and b>=c:
    greatest = b
else:
    greatest = c

print("%i eh o maior"%greatest)
