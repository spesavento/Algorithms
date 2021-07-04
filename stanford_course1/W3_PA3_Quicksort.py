from typing import List

#Global variables:
count_pivot_first, count_pivot_last, count_pivot_med = 0, 0, 0

# Case 1: the FIRST element of the unsorted array is chosen as the pivot element for QuickSort
def getCompsWithFirst(arr: List[int]) -> List[int]:
    global count_pivot_first
    
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        #last element less than p (first elem)
        i = 0 
        count_pivot_first += len(arr) - 1  #O(n)
        
        for j in range(len(arr) - 1):
            #if the element we are exploring is less than the pivot, swap with j
            if arr[j + 1] < arr[0]:
                arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
                #increment first elem larger than p (since we added one more less than p)
                i += 1
        #now swap the pivot with the last elem < pivot (i)
        arr[0], arr[i] = arr[i], arr[0]
        
        #now let's sort the first and second subarrays (<p and >p)
        first_subarray = getCompsWithFirst(arr[:i])
        second_subarray = getCompsWithFirst(arr[i+1:])
        return first_subarray + second_subarray

# Case 2: the LAST element of the unsorted array is chosen as the pivot element for QuickSort
def getCompsWithLast(arr: List[int]) -> List[int]:
    global count_pivot_last
    
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        count_pivot_last += len(arr) - 1  #O(n)
        
        #swap first and last 
        arr[0], arr[-1] = arr[-1], arr[0]
        
        #last element less than p (first elem)
        i = 0 
        
        for j in range(len(arr) - 1):
            #if the element we are exploring is less than the pivot, swap with j
            if arr[j + 1] < arr[0]:
                arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
                #increment first elem larger than p (since we added one more less than p)
                i += 1
        #now swap the pivot with the last elem < pivot (i)
        arr[0], arr[i] = arr[i], arr[0]
        
        #now let's sort the first and second subarrays (<p and >p)
        first_subarray = getCompsWithLast(arr[:i])
        second_subarray = getCompsWithLast(arr[i+1:])
        first_subarray.append(arr[i])
        return first_subarray + second_subarray

"""
Case 3:
Consider the first, middle (or k//2th), and final elements of the given array.
Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot.
Be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine). 

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; 
since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.
"""

def getMiddleIndex(arr: List[int]) -> int:
    #if even, return len(x)/2 - 1
    if len(arr) % 2 == 0:
        return len(arr)//2 - 1
    else: 
        return len(arr)//2
    
def getMedianIndex(arr: List[int], x: int, y: int, z: int) -> int:
    #e.g. 1 4 0  1 - 4 * 1 - 0 < 0 , 1 is median
    #e.g. 1 4 8  1 - 4 * 1 - 8 > 0 , 1 is not median 
    if (arr[x] - arr[y]) * (arr[x] - arr[z]) < 0:
        return x
    #e.g. 1 4 0  1 - 4 * 1 - 0 < 0 , 1 is median
    #e.g. 1 4 8  1 - 4 * 1 - 8 > 0 , 1 is not median 
    elif (arr[y] - arr[x]) * (arr[y] - arr[z]) < 0:
        return y
    else:
        return z

def getCompsWithMedianOfThree(arr: List[int]) -> List[int]:
    global count_pivot_med
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        count_pivot_med += len(arr) - 1
        
        #find the median index of the first, middle and last
        k = getMedianIndex(arr, 0, getMiddleIndex(arr), -1)
        
        #swap with first (if it's not already)
        if k != 0:
            arr[0], arr[k] = arr[k], arr[0]
            
        i = 0
        for j in range(len(arr) - 1):
            #if next elem is less than pivot (which we made the first elem)
            if arr[j + 1] < arr[0]:
                arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1] 
                i += 1
        #swap last smallest with pivot
        arr[0], arr[i] = arr[i], arr[0]
        
        first_part = getCompsWithMedianOfThree(arr[:i])
        second_part = getCompsWithMedianOfThree(arr[i+1:])
        first_part.append(arr[i]) #so that pivot is at end
        return first_part + second_part

#open file
file_arr = open('quicksort.txt', 'r')
#create a list
list_ints = list(map(int, file_arr.read().split('\n')[:-1]))
getCompsWithFirst(list_ints)
file_arr.close()

file_arr = open('quicksort.txt', 'r')
list_ints = list(map(int, file_arr.read().split('\n')[:-1]))
getCompsWithLast(list_ints)
file_arr.close()

file_arr = open('quicksort.txt', 'r')
list_ints = list(map(int, file_arr.read().split('\n')[:-1]))
getCompsWithMedianOfThree(list_ints)
file_arr.close()

#Q1: 162085 comparisons
print("With the pivot as the FIRST element, we have " + str(count_pivot_first) + " comparisons")
#Q2: 164123 comparisons
print("With the pivot as the LAST element, we have " + str(count_pivot_last) + " comparisons")
#Q3: 138382 comparisons
print("With the pivot as the MEDIAN of three elements (first, middle, last), we have " + str(count_pivot_med) + " comparisons")