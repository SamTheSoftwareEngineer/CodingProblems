"""Write a function that returns the intersection of two arrays.

Each element in the result should appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

{ 0:1, 1:2, 2:2, 3:1 }

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Constraints:
Your answer must be in O(n) time complexity. 
You may not use built in functions to solve this problem.

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order."""


def find_intersection(arr1, arr2):
    # Create an answer array and a hashtable that will keep track of
    # how many times an element occurs in arr1
    ans = []
    frequency_map = {}

    # For each number in arr1, we add its count to our frequency map
    for number in arr1:
        frequency_map[number] = frequency_map.get(number, 0) + 1 
    
    # For each element in arr2, we check if the element is in our frequency map
    # and if the count is greater than 0 (this allows us to make sure the element is only
    # added to the result as many times as it appears in both arrays), we append it to the result 
    for element in arr2:
        if element in frequency_map and frequency_map[number] > 0:
            ans.append(element)
            # Decrement our frequency counter 
            frequency_map[number] -= 1
    
    return ans 




print(find_intersection([1,2,3,4], [4,1,5,6])) # [4]
print(find_intersection([1,2,2,1], [2,2])) # [2, 2]
