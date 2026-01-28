# To move all zeros to the end of an array while maintaining the order of non-zero elements

class Solution:
    def pushZerosToEnd(self, arr):
        count = 0 
        n = len(arr)    

        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i] 
                count += 1



arr = [0, 5, 0, 2, 0, 7, 0, 1]
Solution().pushZerosToEnd(arr)
print(arr)

# Output: [5, 2, 7, 1, 0, 0, 0, 0] (all zeros moved to the end)

