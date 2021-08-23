def findLowIndex(arr, start, end, target):
    if end == start:
        if arr[start] > target:
            return start
        else:
            return start + 1
    
    
    mid = start + (end - start) //2
    mid_node = arr[mid]
    
    if target > mid_node:
        return findLowIndex(arr, mid + 1, end, target)
    else:
        return findLowIndex(arr, start, mid, target)
    
file = "algo1-programming_prob-2sum.txt"
extract_lines = [int(line) for line in open(file, "r").readlines()]
arr = sorted(extract_lines)

interval = 10000
n = len(arr) - 1
sum_list = {}
count = 0
for i in arr:
    mySet = set()
    
    i_start = findLowIndex(arr, 0, n, -interval - i)    
    i_end = findLowIndex(arr, 0, n, interval - i)
    
    range_list = arr[i_start:i_end]
        
    if i in range_list:
        range_list.remove(i)
    
    for j in range_list:
        sum_list[i + j] = True
        
list_items = sum_list.items()
print(len(list_items))