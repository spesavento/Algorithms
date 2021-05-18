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
