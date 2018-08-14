""" estimates electricity bills
for:
price per kWh in cents OR TARIFFs,
daily use in kWh,
and number of days in the billing period."""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def main():
    print("|-- Energex Bill Estimator --|")
    tariff = input("Select tariff(Enter 11 or 31):")
#   price = int(input("Enter the cost of power in cents per kWh: " + u'\xa2'))
    useage = float(input("Enter the daily power usage in kWh:"))
    days = int(input("Enter the number of days for the billing period:"))
    if tariff == "11":
        total = TARIFF_11 * useage * days
    else:
        total = TARIFF_31 * useage * days
    print("Estimated Bill: $" + "{:.2f}".format(total))


main()
