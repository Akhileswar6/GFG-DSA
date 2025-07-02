# Finding the maximum subarray sum using kadane's algorithm

class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]
        maxEnding = arr[0]
        
        for i in range(1, len(arr)):
            maxEnding = max(maxEnding + arr[i], arr[i])
            
            res = max(res, maxEnding)
        
        return res


arr = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArraySum(arr))  # Output: 6 (subarray [4,-1,2,1] has the largest sum)