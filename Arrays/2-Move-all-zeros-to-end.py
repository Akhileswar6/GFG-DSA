# To move all zeros to the end of an array while maintaining the order of non-zero elements

class Solution:
    def pushZerosToEnd(self, arr):
        count = 0       # position to place the next non-zero element
        n = len(arr)    

        for i in range(n):
            if arr[i] != 0:                                  # if 5 != 0:                         
                arr[i], arr[count] = arr[count], arr[i]      # arr[1], arr[0] = arr[0], arr[1]    
                count += 1                                   # increment count to 1



arr = [0, 5, 0, 2, 0, 7, 0, 1]
Solution().pushZerosToEnd(arr)
print(arr)


