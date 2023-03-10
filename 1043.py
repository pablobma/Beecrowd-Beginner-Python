values = input().split()
a = float(values[0])
b = float(values[1])
c = float(values[2])

if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
    perimeter = (a + b + c)
    print("Perimetro = %.1f"%perimeter)

else:
    area_trapezium = ((a+b) * c) / 2
    print("Area = %.1f"%area_trapezium)
