# Find all elements in an array that appear more than n/3 times
class Solution:
    def findMajority(self, arr):
        n = len(arr)            # Get the length of the array
        freq = {}               # Dictionary to store frequency of elements 
        res = []                # Result list to store elements that appear more than n/3 times
        
        for ele in arr:                                 # loops through each element in the array
            freq [ele] = freq.get(ele,0) + 1            # Increment the count of the element if it is in the dictionary, otherwise initialize it to 1
            
        for ele, cnt, in freq.items():                  # Iterate through the frequency dictionary      
            if cnt > n//3:                              # Check if the count of the element is greater than n/3 
                res.append(ele)                         # If it is, append the element to the result list
                
        if len(res) == 2 and res[0] > res[1]:           # If there are two elements in the result list, sort them in ascending order
            res[0], res[1] = res[1], res[0]             # Swap the elements if the first is greater than the second
        return res
    

s = Solution()
print(s.findMajority([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        