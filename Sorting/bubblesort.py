# Time Complexity: O(n^2) Space Complexity: O(1)
def bubble_sort(list):
    # Make variables for the last value in the list, set sorted to False (since the input array is guarenteed to be unsorted)
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True 
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i+1], list[i] = list[i], list[i+1]
                sorted = False
        unsorted_until_index -= 1

    return list 

# Examples
print(bubble_sort([60,15,4,3])) # [3,4,15,60]


