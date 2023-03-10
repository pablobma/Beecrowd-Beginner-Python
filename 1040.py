grade = input().split()
grade_1 = float(grade[0])
grade_2 = float(grade[1])
grade_3 = float(grade[2])
grade_4 = float(grade[3])

average = (2*grade_1 + 3*grade_2 + 4*grade_3 + 1*grade_4) / 10

if average > 7:
    print("Media: %.1f" % average)
    print("Aluno aprovado.")
elif average < 5:
    print("Media: %.1f" % average)
    print("Aluno reprovado.")
else:
    exam = float(input())
    print("Media: %.1f" % average)
    print("Aluno em exame.")
    print("Nota do exame: %.1f"%exam)
    if ((exam + average) / 2) >= 5.0:
        print("Aluno aprovado.")
        new_average = ((exam + average) / 2)
        print("Media final: %.1f"%new_average)
    else:
        print("Aluno reprovado.")
        new_average = ((exam + average) / 2)
        print("Media final: %.1f"%new_average)
