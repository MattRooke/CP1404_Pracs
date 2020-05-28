def number_of_blocks(number_of_rows):
    if number_of_rows < 0:
        return 0
    return number_of_rows + number_of_blocks(number_of_rows - 1)


print(number_of_blocks(int(input("How many rows will the pyramid be?"))))
