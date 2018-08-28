numbers = [int(input("Number:")) for i in range(1, 6)]
print(numbers)
average = sum(numbers) / len(numbers)
print("The first number is {}\nThe last number is {}\nThe smallest number is {}\nThe largest number is {}\nThe average "
      "of the numbers is {}".format(numbers[0], numbers[4], min(numbers), max(numbers), average))

