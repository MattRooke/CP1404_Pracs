for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number = int(input("How many stars are in the sky? :"))
for i in range(number):
    print("*", end=" ")
print()

for i in range((number+1)):
    print("*"*i)
