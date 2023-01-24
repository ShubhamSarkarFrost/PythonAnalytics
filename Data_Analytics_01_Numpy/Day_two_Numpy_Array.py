my_list = [1,2,3]
import numpy as np

arr = np.array(my_list)
print("\n")
print(f" Array as a List in Numpy : {arr}")


my_mat = [[1,2,3],[3,4,5],[5,6,7]]
print("\n")
print(f"List of List in Numpy : {np.array(my_mat)}")

################# To Generate a Range of Number #################
rangearr = np.arange(0, 10)  # syntax - np.arange(0 - start index , 10 - end index)
print("\n")
print(f"List of number : {rangearr}")

################# To Generate a Range of Number with Step Size #################
rangeStepSize = np.arange(0, 10, 2)  # syntax - np.arange(0 - start index , 10 - end index, 2 - Step Size)
print("\n")
print(f"Range of Even Number : {rangeStepSize}")

################# To Generate a Single Dimension zero Tuple #################
rangezerosingle = np.zeros(3)
print("\n")
print(rangezerosingle)

################# To Generate a Multi Dimension zero Tuple #################
rangezeromultiple = np.zeros((5,5))
print("\n")
print(rangezeromultiple)

########## Question 1 - To generate a Multi Dimension Array of 2 - rows , 3 - columns ################
rangeOneMulti = np.ones((3,4))
print("\n")
print(rangeOneMulti)

############## To Generate an Evenly Spred Range of Numbers #########################
############# Use np.linspace(start index , end index , noofrange ) #############
linespacerange = np.linspace(0,10,100)
print("\n")
print(linespacerange)

############### Create an Identity Matrix #################################
########## FAQ - an Identity Matrix is a single dimension array of diagonal of 1 and other elements zero #########################
identityMatrixfive = np.eye(5)
print("\n")
print(identityMatrixfive)

################ Create a Random Single dimension array ####################################
############ Use np.random method #########################################
randomFiveArray = np.random.rand(5)
print("\n")
print(randomFiveArray)

################ Create a Random Two dimension array ####################################
randomTwoDimArray = np.random.rand(5,5)
print("\n")
print(randomTwoDimArray)

################# Create an Array of Number , using Gausian distribution ########################
randomGaussArray = np.random.randn(5)
print("\n")
print(randomGaussArray)
################# Create a Random Low Array of Number #################################
randomLowHighArray = np.random.randint(5, 100, 5)
print("\n")
print(randomLowHighArray)
################# To Generate two array with Range of Number  #################
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

print("To Reshape an Array : Use arrayname.reshape(dim, dim) eg: ")
arr_reshape = arr.reshape(5,5)
print("\n")
print(arr_reshape)
print("to Find Max Value of Array use Max for Min use Min")
print("Max Value of an Array : ")
print(ranarr.max())
print("To Find Min Value of an Array")
print(ranarr.min())
print("To Find Index of Max and Min Value use argmax & argmin")
print(f"Index of the Maximum Value of Array {ranarr} is {ranarr.argmax()}")
print(f"Index of the Minimum Value of Array {ranarr} is {ranarr.argmin()}")
print(f"To Know the shape of the Array {ranarr} use shape method : {ranarr.shape}")