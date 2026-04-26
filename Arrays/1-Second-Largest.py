def getSecondLargest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num

        elif first > num > second:
            second = num

    return second if second != float('-inf') else -1

        

print(getSecondLargest([23,87,65,12,34,89,90]))  
