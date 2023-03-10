salary = float(input())

if 0.00 <= salary <= 2000.00:
    print("Isento")

elif 2000.01 <= salary <= 3000.00:
    p = salary - 2000.00
    taxes = 0.08*p
    print("R$ %.2f"%taxes)

elif 3000.01 <= salary <= 4500.00:
    n = 1000
    m = salary - 3000.00
    taxes_2 = (0.08*n) + (0.18*m)
    print("R$ %.2f"%taxes_2)

elif 4500.00 < salary:
    a = salary - 4500
    taxes_3 = (1000*0.08) + (1500*0.18) + (a*0.28)

    print("R$ %.2f"%taxes_3)