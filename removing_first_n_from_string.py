# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n 
# Then, return a new string.

def remove_chars(word, n):
    print('Original string character:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("engineering", 7))
print(remove_chars("engineering", 4))
