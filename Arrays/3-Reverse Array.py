# Reverse an array in place

# Approach-1
# class Solution:
#     def reverseArray(self, arr):
#         left = 0
#         right = len(arr) -1

#         while left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left +=1
#             right -=1
#         return arr


# s = Solution()
# print(s.reverseArray([87,12,65,0,23,34,89,90]))


# Approach-2
class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        
        for i in range(n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        return arr

s = Solution()
print(s.reverseArray([87,12,65,0,23,34,89,90,198]))
    
