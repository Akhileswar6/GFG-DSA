# Given an array of size N, rotate it by D elements in counter-clockwise direction.

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)        # gets the length of the array
        
        d %= n              # handles cases where d is greater than n
        
        reverse(arr, 0, d - 1)    # Reverses the first d elements
        reverse(arr, d, n - 1)    # Reverses the remaining n-d elements
        reverse(arr, 0, n - 1)    # Reverses the entire array to get the final rotated array
        
        
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
            
            
        
            
        
        
    