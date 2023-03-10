values = input().split()
start = int(values[0])
end = int(values[1])

if start == end:
    print("O JOGO DUROU 24 HORA(S)")
elif start < end:
    formula = end - start
    print("O JOGO DUROU %i HORA(S)"%formula)
else:
    formula_2 = 24 - start + end
    print("O JOGO DUROU %i HORA(S)"%formula_2)
