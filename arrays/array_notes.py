import copy
import bisect

### Instantiating a list
l_init1 = [3, 5, 7, 11]
print(l_init1) 
#[3, 5, 7, 11]

l_init2 = [1] + [0] * 10
print(l_init2) 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

l_init3 = list(range(5))
print(l_init3) 
#[0, 1, 2, 3, 4]

### List operations
A = [2, 8, 5, 4, 2]
len(A) 
#5
A.append(42)
# [2, 8, 5, 4, 2, 42]

A.remove(2) #removes first 2 seen
# [8, 5, 4, 2, 42]

A.insert(3, 28)
#[8, 5, 4, 28, 2, 42]

### 2D arrays
arr_2d = [[1, 2, 4], [3, 5, 7, 9], [13]]
print(arr_2d)

print(5 in A) #O(n)

copy_me = [1,2,3,4]
copied = copy_me
print(copied)
#[1, 2, 3, 4]
#altering copied will alter original since they are pointing to same list
copied.append(5)
print(copy_me)
#[1, 2, 3, 4, 5]

copy_me = [1,2,3,4]
shallow_copy = copy.copy(copy_me)
shallow_copy.append(5)
shallow_copy.remove(2)
print(shallow_copy)
#[1, 2, 3, 4, 5]
print(copy_me)
#[1, 2, 3, 4]

copy_me = [1,2,3,4]
deep_copy = copy.deepcopy(copy_me)
deep_copy.append(5)
deep_copy.remove(2)
print(deep_copy)
print(copy_me)

copy_me = [1,2,3,4]
a = list(copy_me)
a.append(5)
a.remove(2)
print(a)
print(copy_me)

A = [1,2,3,9,10]
#Locate the insertion point for x in a to maintain sorted order.
print(bisect.bisect(A, 6))
A = [1,2,3,9,10]

print(min(A)) #1
print(max(A)) #10

A.reverse() #in-place
print(A) #[10, 9, 3, 2, 1]

A = [1,2,3,9,10]
rev_A = list(reversed(A))  #copy
print(rev_A) #[10, 9, 3, 2, 1]
print(A) #[1, 2, 3, 9, 10]

A = [1,6,2,8,4,0]
A.sort() #in-place
print(A) #[0, 1, 2, 4, 6, 8]
A = [1,6,2,8,4,0]
A_sorted = list(sorted(A))  #copy
print(A_sorted) #[0, 1, 2, 4, 6, 8]
print(A) #[1, 6, 2, 8, 4, 0]

del A[2] #deletes the i-th element
print(A) #[1, 6, 8, 4, 0]

del A[1:3] #removes the slice from 1 UP TO 3
print(A) #[1, 4, 0]

### Slicing
#A[i:j:k] where i, j and k are optional
A = [1, 6, 3, 4, 5, 2, 7]
A[2:4] #index 2 UP TO 4 (2 and 3) --> [3, 4]
A[2:] #2 through end of array --> [3, 4, 5, 2, 7]
A[:4] #beginning UP TO 4 --> [1, 6, 3, 4]
A[:-1] #beginning UP TO last element --> [1, 6, 3, 4, 5, 2]
A[-3:] #3 from end through end --> [5, 2, 7]
A[-3:-1] #3 from end UP TO last element --> [5, 2]
A[1:5:2] #1 UP TO 5, every other --> [6, 4]
A[5:1:-2] #5 DOWN TO 1, every other --> [2, 4]
A[::-1] #whole list, but -1 revesal --> [7, 2, 5, 4, 3, 6, 1]

B = A[2:] + A[:2] #rotates list A by k to the left (wrap around)
print(B) #[3, 4, 5, 2, 7, | 1, 6]

B = A[:] #shallow copy

### List compression
[x**2 for x in range(6)] #[0, 1, 4, 9, 16, 25
[x**2 for x in range(6) if x%2 == 0]  #[0, 4, 16]
#can be rewritten with map(), filter(), lambdas, but this is clear

#loops
A = [1, 3, 5]
B = ['a', 'b']
[(x, y) for x in A for y in B]
#[(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')].

#2D to 1D
M = [['a', 'b', 'c'], ['d', 'e', 'f']]
#x for row in M for x in row creates ['a', 'b', 'c', 'd', 'e', 'f ']

#iterate over a 2D list
A = [[1, 2, 3], [4, 5, 6]] 
#then 
[[x ** 2 for x in row] for row in A]
#yields [[1, 4, 9], [16, 25, 36]]

A = [5,6,3,2,7]
for i, num in enumerate(A):
    print(i)
    print(num)