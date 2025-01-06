"""Write a function that accepts an array of strings and returns the first duplicate value it finds

Example:
Input: ['a','b','c','d','c','e','f']
Output: 'c' 

Assume there is always one pair of duplicates in the array

Make sure you answer is in O(n) time complexity"""

def find_duplicates(arr):
    # Initialize an empty hashmap to store characters and the amount of times they occur
    char_count = {}

# For each character in the array, we map it to its count
    for char in arr:
        char_count[char] = char_count.get(char, 0) + 1
        # If the character's count is greater than 1 (meaning there's a duplicate), we return it 
        if char_count[char] > 1:
            return char 

print(find_duplicates(['a','b','c','d','c','e','f'])) # c 
print(find_duplicates(['a', 'b', 'a', 'b'])) # a