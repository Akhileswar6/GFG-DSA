# Reverse an array in place

# Approach-1
class Solution:
    def reverseArray(self, arr):
        left = 0                                                    # Holds the index of the first element
        right = len(arr) -1                                         # Holds the index of the last element

        while left < right:                                         # loop until the two pointers meet
            arr[left], arr[right] = arr[right], arr[left]           # arr[87], arr[90] = arr[90], arr[87]

            left +=1                                                # increment the left pointer
            right -=1                                               # decrement the right pointer
        return arr


s = Solution()
print(s.reverseArray([87,12,65,0,23,34,89,90]))


# Approach-2
class Solution:
    def reverseArray(self, arr):
        n = len(arr)                                              # Get the length of the array
        
        for i in range(n//2):                                     # Loop through the first half of an array
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]               # arr [87], arr[9-0-1] = arr[9-0-1], arr[87]
        return arr

s = Solution()
print(s.reverseArray([87,12,65,0,23,34,89,90,198]))
    
