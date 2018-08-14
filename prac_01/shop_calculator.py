""" calulates the toatl price of items entered by user,
if total is > $100 10% discount is applied """


def main():
    num_of_items = int(input("Number of items:"))
    total = 0.00
    while num_of_items == 0:
        print("Invalid number of items!")
        num_of_items = int(input("Number of items:"))
    for i in range(1, num_of_items+1):
        item_value = float(input("Item " + str(i) + " value: $"))
        while item_value < 0:
            print("Invalid value of item!")
            item_value = float(input("Item " + str(i) + " value: $"))
        total += item_value
    if total > 100:
        total -= total * .1
    print("Total cost for", i, "items is: ${:.2f}".format(total))


main()
