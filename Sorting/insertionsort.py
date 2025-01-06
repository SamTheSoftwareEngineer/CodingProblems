# Time Complexity --> O(n) Space Complexity --> 0(1)
def insertion_sort(list):
    for index in range(1, len(list)):
        # Save the value that we are "removing" in a temp variable
        temp_value = list[index]
        # The position will represent each value we compare against the temp value 
        position = index - 1

        while position >= 0:
            # If we find that the number at our indicated position is greater than the one we are removing 
            if list[position] > temp_value:
                # Shift the left value to the right 
                list[position + 1] = list[position]
                # Decremenet position by 1 to compare the next left value against the temp value in our next iteration
                position = position - 1 
            else:
                # If we encounter a value at position that is greater than or equal to the temp_value,
                #  it's time to move the temp_value into the gap, so we break the loop 
                break
            # Move the temp value into the gap 
            list[position + 1] = temp_value

    return list 




print(insertion_sort([5,7,2,1]))