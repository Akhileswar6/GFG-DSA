# Given an integer array, find the maximum product of a contiguous subarray.
# The product of a subarray is the result of multiplying all the elements together.
class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        
        currMax = arr[0]
        
        currMin = arr[0]
        
        maxProd = arr[0]
        
        for i in range(1, n):
            
            temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)
            
            currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)
            
            currMax = temp
            
            maxProd = max(maxProd, currMax)
       
        return maxProd

s = Solution()
print(s.maxProduct([2,8,-9,0,3,-2,8]))
