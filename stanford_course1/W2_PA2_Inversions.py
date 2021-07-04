"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
"""
from typing import List

#1235 4678
def mergeCount(b: List[int], c: List[int]) -> [List[int], int]:
    num_inverses = 0
    arr = []
    
    while len(b) > 0 or len(c) > 0:
        if len(b) > 0 and len(c) > 0:
            if b[0] < c[0]:
                arr.append(b[0])
                b = b[1:]
            else:
                arr.append(c[0])
                c = c[1:]
                num_inverses += len(b)
        elif len(b) > 0:
            arr.append(b[0])
            b = b[1:]
        elif len(c) > 0:
            arr.append(c[0])
            c = c[1:]
            
    return arr, num_inverses
            
    
def sortCount(a: List[int]) -> [List[int], int]:
    arr_len = len(a)
    if arr_len <= 1:
        return a, 0
    b, invx = sortCount(a[:(arr_len//2)]) #sort first half
    c, invy = sortCount(a[(arr_len//2):]) #sort second half
    d, invz = mergeCount(b, c) #merge the two sorted halves together
    
    return d, invx + invy + invz
    
    
#Test cases
t1 = [1,3,5,2,4,6]
#1235 4678
print("Testing with:", t1)
print("Expecting:", 3)
print("Returned:", sortCount(t1)[1])

t2 = [1,5,3,2,4]
print("Testing with:", t2)
print("Expecting:", 4)
print("Returned:", sortCount(t2)[1])

t3 = [5,4,3,2,1]
print("Testing with:", t3)
print("Expecting:", 10)
print("Returned:", sortCount(t3)[1])

t4 = [1,6,3,2,4,5]
print("Testing with:", t4)
print("Expecting:", 5)
print("Returned:", sortCount(t4)[1])

t5 = [ 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
print("Testing with:", t5)
print("Expecting:", 56)
print("Returned:", sortCount(t5)[1])

t6 = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 ]
print("Testing with:", t6)
print("Expecting:", 590)
print("Returned:", sortCount(t6)[1])

file_arr = open('IntegerArray.txt', 'r')
#create a list
list_ints = list(map(int,file_arr.read().split('\n')[:-1]))
file_arr.close()
print(sortCount(list_ints)[1])
#2407905288
