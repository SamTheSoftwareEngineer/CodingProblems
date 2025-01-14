"""Use recursion to write a function that accepts an array of strings and returns the total number
of characters across all the strings. For example, if the input array is ['ab', 'c', 'def', 'ghij' ],
the output should be 10 since there are 10 characters in total. """

def totalnumberofchars(arr):
    if len(arr) == 1:
        return 1 
    
    # Return the total number of characters in the first string plus the total number of characters in the remaining strings
    return len(arr[0]) + totalnumberofchars(arr[1:])

