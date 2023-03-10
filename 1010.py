product_1 = input().split()
code_1 = int(product_1[0])
units_1 = int(product_1[1])
price_1 = float(product_1[2])

product_2 = input().split()
code_2 = int(product_2[0])
units_2 = int(product_2[1])
price_2 = float(product_2[2])

result = (units_1 * price_1) + (units_2 * price_2)

print("VALOR A PAGAR: R$ %.2f"%result)
