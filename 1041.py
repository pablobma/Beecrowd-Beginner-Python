value = input().split()
value_x = float(value[0])
value_y = float(value[1])

if value_x == 0 and value_y == 0:
    print("Origem")
elif value_x > 0 and value_y > 0:
    print("Q1")
elif value_x < 0 and value_y > 0:
    print("Q2")
elif value_x < 0 and value_y < 0:
    print("Q3")
elif value_x > 0 and value_y < 0:
    print("Q4")
elif value_x == 0:
    print("Eixo Y")
elif value_y == 0:
    print("Eixo x")
