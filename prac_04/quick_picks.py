""""Generates lines of random numbers"""

import random

LOWEST_RANGE = 1
HIGHEST_RANGE = 46
NUMBERS_GENERATED = 6


def main():
    number_of_picks = int(input("How many quick picks? :"))
    for i in range(number_of_picks):
        picks = []
        while len(picks) < NUMBERS_GENERATED:
            random_number = random.randint(LOWEST_RANGE, HIGHEST_RANGE)
            if random_number not in picks:
                picks.append(random_number)
        picks.sort()
        output = " ".join(str(numbers) for numbers in picks)
        print(output)


main()
