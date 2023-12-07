def length_of_last_word(s):
    # Splitting the string into a list of words
    words = s.split()

    if not words:
        return 0

    return len(words[-1])


test_string = input()
result = length_of_last_word(test_string)
print(f"The length of the last word is: {result}")