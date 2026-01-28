# To find the second largest number in an array

class Solution:
    def getSecondLargest(self, arr):
        first = second = float('-inf')
        for num in arr:
            if num > first:
                second = first
                first = num

            elif first > num > second:
                second = num

        return second

        

s = Solution()
print(s.getSecondLargest([23,87,65,12,34,89,90]))  
