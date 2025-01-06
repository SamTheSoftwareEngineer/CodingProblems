"""Write a function that accepts a string that contains all the letters of the alphabet except one and returns the 
missing letter.

Example:
Input: "The quick brown box jumps over a lazy dog"
Output: f

Your answer should have a time complexity of O(n)
"""

def missing_letter(string):
    # Create a list of all the letters in the alphabet
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Create a set of all the letters in the string
    string_letters = set(string.lower())

    # Loop through the alphabet and check if each letter is in the string
    for letter in alphabet:
        # If the letter is not in the string, return it
        if letter not in string_letters:
            return letter

    # If all letters are in the string, return None
    return None

# Examples
print(missing_letter('The quick brown box jumps over a lazy dog')) # f
print(missing_letter('abcdefghijklmnopqrstuvwxyz')) # None

