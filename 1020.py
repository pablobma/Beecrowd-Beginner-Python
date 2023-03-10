days = int(input())

years = days // 365
months = (days%365) // 30
day_s = (days%365)%30

print("%i ano(s)"%years)
print("%i mes(es)"%months)
print("%i dia(s)"%day_s)
