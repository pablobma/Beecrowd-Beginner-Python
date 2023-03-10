import math

values = input().split()
x1 = float(values[0])
y1 = float(values[1])

values_2 = input().split()
x2 = float(values_2[0])
y2 = float(values_2[1])

Distance = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

print("%.4f" % Distance)
