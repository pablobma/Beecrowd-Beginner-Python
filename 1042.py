numbers = input().split()
first = int(numbers[0])
second = int(numbers[1])
third = int(numbers[2])

sequence = sorted([first, second, third])
for position in sequence:
    print(position)

print("\n%i"%first)
print(second)
print(third)
