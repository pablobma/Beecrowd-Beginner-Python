import math

samples = input().split()
A = float(samples[0])
B = float(samples[1])
C = float(samples[2])

if A == 0.0:
    print("Impossivel calcular")
elif (B*B - 4*A*C) < 0:
    print("Impossivel calcular")
else:
    bhaskara_1 = (B * -1 + (math.sqrt(pow(B, 2) - 4 * A * C))) / (2 * A)
    bhaskara_2 = (B * -1 - (math.sqrt(pow(B, 2) - 4 * A * C))) / (2 * A)

    print("R1 = %.5f"%bhaskara_1)
    print("R2 = %.5f"%bhaskara_2)
