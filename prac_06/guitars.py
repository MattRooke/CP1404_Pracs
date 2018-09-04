from prac_06.guitar import Guitar

guitars = []
name = input("Name: ")
while name:
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")
    print(, "added")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))


for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
