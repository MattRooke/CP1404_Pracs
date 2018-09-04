from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2012, 100.00)

print(gibson.name, "get_age() - Expected 96. Got", gibson.get_age())
print(another.name, "get_age() - Expected 6. Got", another.get_age())
print(gibson.name, "is_vintage() - Expected True. Got", gibson.is_vintage())
print(another.name, "is_vintage() - Expected False. Got", another.is_vintage())


