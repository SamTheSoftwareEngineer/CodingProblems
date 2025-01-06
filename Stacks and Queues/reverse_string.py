"""Write a function that uses a stack to reverse a string.

Example:
Input: "The quick brown fox jumps over the lazy dog"
Output: "god yzal eht revo spmuj xof nworb kciuq The"

Your answer should have a time complexity of O(n)
"""

def reverse_string(string):
    # Initialize an empty stack
    stack = []

    # Push each letter of the string into the stack
    for letter in string:
        stack.append(letter)

    # Initialize an empty string
    reversed_string = ""

    # Pop each letter off the stack and add it to the reversed string
    for _ in range(len(stack)):
        reversed_string += stack.pop()
    
    # Return the reversed string
    return reversed_string



print(reverse_string('abcde')) #edcba