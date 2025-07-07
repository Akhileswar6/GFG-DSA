# To find the second largest number in an array

class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
           return -1        # returns -1 if there are less than 2 elements
           
        first = second = float('-inf')
        for num in arr:
            if num > first:          # if 23 > first:
                second = first       # second = ('-inf')
                first = num          # first = 23
            elif num > second and num != first:    # if 65 > 23  and 65 != 87:
                second = num                       # second = 65
                
        if second == float('-inf'):     # if second = -inf
            return -1                   # return -1 if no second largest found
        else:
            return second

s = Solution()
print(s.getSecondLargest([23,87,65,12,34,89,90]))  
