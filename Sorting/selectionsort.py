# Time Complexity: O(n^2) Space Complexity: O(1)
def selection_sort(list):
    # Loop through the array
    for i in range(len(list) - 1):
        # Assume the current lowest number's index is the current index
        lowest_number_index = i
        for j in range(i+1, len(list)):
            # Check if the next element is lower than that at the lowest number's index (meaning we found a smaller number)
            if list[j] < list[lowest_number_index]:
                # Update the lowest number's index to be the ith + 1 index (j)
                lowest_number_index = j 
            # Swap the two values 
        list[i], list[lowest_number_index] = list[lowest_number_index], list[i]
    
    return list 
        



print(selection_sort([2,6,1,3]))