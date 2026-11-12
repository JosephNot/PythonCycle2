def binary_search(data, target): 
    low = 0 
    high = len(data) - 1 
    while low <= high: 
        mid = (low + high) // 2 
        if data[mid] == target: 
            return mid 

        elif data[mid] < target: 
            low = mid + 1 

        else: 
            high = mid - 1 

    return -1 

 
numbers = [3, 5, 7, 8, 12, 14] 

print(binary_search(numbers, 12)) 

def linear_search(needle, haystack): 

    for searchcount in range(len(haystack)): 
        if haystack[searchcount] == needle: 
            return searchcount 

    return -1 

 
print(linear_search(21, [7, 14, 21, 28])) 