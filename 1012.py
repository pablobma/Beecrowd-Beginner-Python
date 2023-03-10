values = input().split()
A = float(values[0])
B = float(values[1])
C = float(values[2])

pi = 3.14159

triangle = (A * C)/2
circle = pi * pow(C, 2)
trapezium = (A + B)*C / 2
square = B * B
rectangle = A * B

print("TRIANGULO: %.3f"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3F"%trapezium)
print("QUADRADO: %.3f"%square)
print("RETANGULO: %.3f"%rectangle)
