dia, date_1 = input().split()
date_1 = int(date_1)
h1, m1, s1 = map(int, input().split(":"))

dia_2, date_2 = input().split()
date_2 = int(date_2)
h2, m2, s2 = map(int, input().split(":"))

h = h2 - h1
m = m2 - m1
s = s2 - s1
date = date_2 - date_1

if s < 0:
    s = s + 60
    m = m - 1

if m < 0:
    m = m + 60
    h = h - 1

if h < 0:
    h = h + 24
    date = date - 1

print(date, "dia(s)")
print(h, "hora(s)")
print(m, "minuto(s)")
print(s, "segundo(s)")
