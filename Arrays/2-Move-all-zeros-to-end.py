

def pushZerosToEnd(arr):
    count = 0 
    n = len(arr)    

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i] 
            count += 1

    return arr

print(pushZerosToEnd([0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]))





