import wikipedia

user_input = input("Search Wikipedia:")
while user_input != '':
    print("Searching... beep... boop...")
    summary = wikipedia.summary(user_input)
    print(user_input, "Summary:\n {}".format(summary))
    user_input = input("Search Wikipedia:")
print("Done.")
