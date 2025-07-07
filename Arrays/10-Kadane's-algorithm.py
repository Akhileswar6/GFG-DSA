# Finding the maximum subarray sum using kadane's algorithm

class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]                  # initializing result with the first element
        maxEnding = arr[0]            # maxEnding keeps track of the maximum sum ending at the current position  
        
        for i in range(1, len(arr)):                            # for loop through the array starting from the second element
            maxEnding = max(maxEnding + arr[i], arr[i])         # maxEnding = max(-2 + 1, 1) = 1
            res = max(res, maxEnding)                           # res = max(1, 1) = 1
        
        return res


arr = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()                                           # Create an instance of the Solution class
print(solution.maxSubArraySum(arr))  # Output: 6 (subarray [4,-1,2,1] has the largest sum)