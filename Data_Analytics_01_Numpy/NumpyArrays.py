import numpy as np


# Numpy Arrays are of Two Type - One dimensional and two dimensional
# ###### Single List Transformation #######
# my_list = [1,2,3]
# listasArray = np.array(my_list)
# print(type(listasArray))
# print(f" Array as a List {listasArray}")
#
# ###### Multiple List Transformation #######
# my_mat = [[1,2,3],[3,4,5],[5,6,7]]
# MulListArray = np.array(my_mat)
# print(f" Multiple Array as a List {MulListArray}")
############# <-range function ->#####################
# print(f"Range of the Data from 0 - 10 with step of 2 is :{np.arange(0,10,2)}")
############<- to create a array of 0. ->################
# print(f"Single Dimesional Array with Zeros : {np.zeros(3)}")
# print(f"Double Dimensional Array with zeros : {np.zeros((5,5))}")
######### to create an array with ones we can use np.ones #########
# print(f"Double Dimensional Array with ones : {np.ones((5,5))}")
######### to create evenly spaced point between the number use np.linspace(start num , stop num , evenspread num)
# print(f"Evenly Spaced Num {np.linspace(0,5,100)}")
########## to create a identity matrix  use np.eye(no of rows) ####################
# print(f"{np.eye(5)}")
########## To create a Random Number of universally random digits use np.random.rand(noofnums) #############
# print(f"{np.random.rand(5)}")
########## To create a Random Number of standard normal distributon use np.random.randn(noofnums) #############
# print(f"{np.random.randn(4,4)}")
########## To create a Random Integers of standard normal distributon use np.random.randint(noofnums) #############
print(f"{np.random.randint(1,100,10)}")




