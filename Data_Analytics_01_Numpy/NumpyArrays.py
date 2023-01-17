import numpy as np


###### Single List Transformation #######
my_list = [1,2,3]
listasArray = np.array(my_list)
print(type(listasArray))
print(f" Array as a List {listasArray}")

###### Multiple List Transformation #######
my_mat = [[1,2,3],[3,4,5],[5,6,7]]
MulListArray = np.array(my_mat)
print(f" Multiple Array as a List {MulListArray}")