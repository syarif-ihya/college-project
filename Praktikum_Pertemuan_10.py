import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print(arr + arr)
print(arr * arr)
print(arr / arr)

list = [1,2.0,3,4,5]

print(list)
print(type(list))

print(arr.mean())
print(arr.sum())

print(arr[1])
print(arr[2:5])
print(arr[0])

print("\n")

arr = np.array([[1,2,3], ['a','b','c']])



print("\n")

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print(arr)
print(arr.ndim) 

print("\n")

arr = np.array([[[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]],[[["a","b"],["c",'d']],[['e','f'],['g','h']],[['i','j'],['k','l']]]])
print(arr)
print(arr.ndim) 

arr= np.array([True, True, False, 5, 10.5, 'True'])
print(arr.dtype)
arr= np.array([True, True, False, 1, 2.0])
print(arr.dtype)
arr= np.array([True, True, False, 1])
print(arr.dtype)
arr= np.array([True, True, False])
print(arr.dtype)

# Bool ->
