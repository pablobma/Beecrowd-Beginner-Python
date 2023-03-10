a, b, c, d = list(map(int, input().split()))

minute = d - b
hour = c - a

if minute < 0:
    minute = minute + 60
    hour = hour - 1

if hour < 0:
    hour = hour + 24

if minute == 0 and hour == 0:
    minute = 0
    hour = 24


print("O JOGO DUROU %i"%hour, "HORA(S) E %i"%minute, "MINUTO(S)")