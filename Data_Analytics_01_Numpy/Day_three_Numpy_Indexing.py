import numpy as np

sample_arr = np.arange(0, 11)
print(f"Sample Array is {sample_arr}")

############ Slice a Single Element #########
arr_new = sample_arr[8]
print("Subset of a Single Element \n")
print(arr_new)

############# Slice a Sub-Set of Element ##########
arr_subset = sample_arr[2:5]
print("Subset of Multiple Element \n")
print(arr_subset)
