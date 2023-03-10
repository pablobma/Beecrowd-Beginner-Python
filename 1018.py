N = int(input())

bank_100 = N // 100
bank_50 = (N % 100) // 50
bank_20 = ((N%100) % 50) // 20
bank_10 = (((N%100)%50)%20) // 10
bank_5 = ((((N%100)%50)%20)%10) // 5
bank_2 = (((((N%100)%50)%20)%10)%5) // 2
bank_1 = ((((((N%100)%50)%20)%10)%5)%2) // 1

print(N)
print("%i nota(s) de R$ 100,00" % bank_100)
print("%i nota(s) de R$ 50,00" % bank_50)
print("%i nota(s) de R$ 20,00" % bank_20)
print("%i nota(s) de R$ 10,00" % bank_10)
print("%i nota(s) de R$ 5,00" % bank_5)
print("%i nota(s) de R$ 2,00" % bank_2)
print("%i nota(s) de R$ 1,00" % bank_1)


