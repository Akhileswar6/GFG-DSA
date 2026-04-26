# Approach-1
def reverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverseArray([87,12,65,0,23,34,89,90]))


# Approach-2
def reverseArray(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    return arr
   

print(reverseArray([87,12,65,0,23,34,89,90,198]))

