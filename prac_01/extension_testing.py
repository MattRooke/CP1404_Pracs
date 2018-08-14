import math

x = 1
y = 100

for i in range(x, y + 1):
    num = math.sqrt(i) % 1
    if num == 0:
        print(i, end=" ")