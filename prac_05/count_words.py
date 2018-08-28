""""Test String
this is a test string to test the number of words counted is the to a a
{num: word for num, word in enumerate(input_text)}
"""

input_text = input("String:")
word_in_string = input_text.split(" ")
print(word_in_string)
word_count = {}
for word in word_in_string:
    count = word_in_string.count(word)
    word_count[word] = count
for key, value in sorted(word_count.items()):
    print("{} : {}".format(key, value))

