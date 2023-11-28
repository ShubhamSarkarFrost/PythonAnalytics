import numpy as np

arr = np.arange(0,11)
print(arr[4])
print(f"Range of a number:{arr[1:5]}")
print(f"Upto a range :{arr[5:]}")
arr[0:5] = 100
print(f"slice of an array : {arr[0:6]}")
print(f"Slice but grab everything : {arr[:]}")
arr[:] = 99
print(arr)
arr_copy = arr.copy()
print(f"Copied Array : {arr_copy}")
arr_2d = np.array([[5,10,15],[20,25,13],[35,10,5]])
print(arr_2d)
print(arr_2d[2,2])
print("Subset of a DD Array \n")
print(arr_2d[:2,1:])
print("Starting Subset of a DD Array \n")
print(arr_2d[:2])
new_array = np.arange(1,11)
print(f"No Greater than 5 {new_array>5}")
np_boolean = new_array > 5
print(f"Array from boolean : {new_array[np_boolean]}")
arr_2d_new = np.arange(50).reshape(5,10)
print(arr_2d_new)
print("Grab a Slice \n")
print(arr_2d[1:3,1:3])