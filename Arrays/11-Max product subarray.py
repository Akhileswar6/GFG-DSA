# Given an integer array, find the maximum product of a contiguous subarray.
# The product of a subarray is the result of multiplying all the elements together.
class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        
        currMax = arr[0]            # Tracks the maximum product ending at the current position
        
        currMin = arr[0]            # Tracks the minimum product ending at the current position (to handle negative numbers)
        
        maxProd = arr[0]            # Initialize maxProd with the first element
        
        for i in range(1, n):       # iterate through the array starting from the second element
            
            temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)                  # Calculate the maximum product ending at the current position
            
            currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)            # Calculate the minimum product ending at the current position
            
            currMax = temp                        # Update currMax with the calculated maximum
            
            maxProd = max(maxProd, currMax)       # Update maxProd with the maximum product found so far
       
        return maxProd

s = Solution()
print(s.maxProduct([2,8,-9,0,3,-2,8]))
