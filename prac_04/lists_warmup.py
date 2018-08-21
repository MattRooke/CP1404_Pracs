"""
numbers[0] = 3
numbers[-1] = 9
numbers[3] = 1
number[:-1] = [3, 1 ,4, 1, 5]
numbers[3:4] = [1]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 6, 5, 3]
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] = 10

numbers[6] = 1

elements = numbers[2:]

print(numbers)

print(elements)

print(9 in numbers)
