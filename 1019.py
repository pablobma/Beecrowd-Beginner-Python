N = int(input())

hours = N//3600
minutes = (N%3600)//60
seconds = (N%3600)%60

print("%i:"%hours + "%i:"%minutes + "%i"%seconds)



