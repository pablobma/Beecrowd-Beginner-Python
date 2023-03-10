import math
N = float(input())

bank_100 = (N // 100)
bank_50 = (N % 100) // 50
bank_20 = ((N%100) % 50) // 20
bank_10 = (((N%100)%50)%20) // 10
bank_5 = ((((N%100)%50)%20)%10) // 5
bank_2 = (((((N%100)%50)%20)%10)%5) // 2

total_coins = N - math.trunc(N) + 0.0001

coin_1 = (((((N%100)%50)%20)%10)%5)%2
coin_050 = (((((((total_coins%100)%50)%20)%10)%5)%2)%1) // 0.5
coin_025 = ((((((((total_coins%100)%50)%20)%10)%5)%2)%1)%0.5) // 0.25
coin_010 = (((((((((total_coins%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25) // 0.10
coin_005 = ((((((((((total_coins%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.10) // 0.05
coin_001 = (((((((((((total_coins%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.10)%0.05) // 0.01

print("NOTAS:")
print("%.i nota(s) de R$ 100.00" % bank_100)
print("%.i nota(s) de R$ 50.00" % bank_50)
print("%.i nota(s) de R$ 20.00" % bank_20)
print("%.i nota(s) de R$ 10.00" % bank_10)
print("%.i nota(s) de R$ 5.00" % bank_5)
print("%.i nota(s) de R$ 2.00" % bank_2)
print("MOEDAS:")
print("%.i moeda(s) de R$ 1.00" % coin_1)
print("%.i moeda(s) de R$ 0.50" % coin_050)
print("%.i moeda(s) de R$ 0.25" % coin_025)
print("%.i moeda(s) de R$ 0.10" % coin_010)
print("%.i moeda(s) de R$ 0.05" % coin_005)
print("%.i moeda(s) de R$ O.O1" % coin_001)