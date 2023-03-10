salary = float(input())

if 0 < salary <= 400:
    new_salary = 1.15*salary
    readjustment = new_salary - salary
    print("Novo salario: %.2f"%new_salary)
    print("Reajuste ganho: %.2f"%readjustment)
    print("Em percentual: 15 %")
elif 400.01 <= salary <= 800:
    new_salary_2 = 1.12*salary
    readjustment_2 = new_salary_2 - salary
    print("Novo salario: %.2f"%new_salary_2)
    print("Reajuste ganho: %.2f"%readjustment_2)
    print("Em percentual: 12 %")
elif 800.01 <= salary <= 1200:
    new_salary_3 = 1.1*salary
    readjustment_3 = new_salary_3 - salary
    print("Novo salario: %.2f" % new_salary_3)
    print("Reajuste ganho: %.2f" % readjustment_3)
    print("Em percentual: 10 %")
elif 1200.01 <= salary <= 2000:
    new_salary_4 = 1.07*salary
    readjustment_4 = new_salary_4 - salary
    print("Novo salario: %.2f" % new_salary_4)
    print("Reajuste ganho: %.2f" % readjustment_4)
    print("Em percentual: 7 %")
else:
    new_salary_5 = 1.04*salary
    readjustment_5 = new_salary_5 - salary
    print("Novo salario: %.2f" % new_salary_5)
    print("Reajuste ganho: %.2f" % readjustment_5)
    print("Em percentual: 4 %")
