item = input().split()
code_x = int(item[0])
quantity_y = int(item[1])

if code_x == 1:
    value = float(4 * quantity_y)
    print("Total: R$ %.2f"%value)
elif code_x == 2:
    value_2 = float(4.5 * quantity_y)
    print("Total: R$ %.2f"%value_2)
elif code_x == 3:
    value_3 = float(5 * quantity_y)
    print("Total: R$ %.2f"%value_3)
elif code_x == 4:
    value_4 = float(2 * quantity_y)
    print("Total: R$ %.2f"%value_4)
elif code_x == 5:
    value_5 = float(1.5 * quantity_y)
    print("Total: R$ %.2f"%value_5)
