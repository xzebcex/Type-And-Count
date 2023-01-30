# Type And Count

# Prompt the user to start typing
line = input('Start typing: ')

# Count the number of spaces in the input and add 1 for the last word
total_words = line.count(' ') + 1

# Print the total number of words
print(total_words)
