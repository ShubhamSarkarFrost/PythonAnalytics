import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = np.arange(1, 4)
my_country = ['USA', 'JAPAN', 'GERMANY']
my_country_2 = ['USA', 'ITALY', 'GERMANY']
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 10}

print("Series of a Number \n")
print(pd.Series(data=my_data))
print("Setting Labels to a Series \n")
print(pd.Series(my_data, labels))
print(pd.Series(my_country, my_data))
new_series = pd.Series(my_data, my_country)
new_series_2 = pd.Series(my_data,my_country_2)
print(new_series)
print(f"get first country index : {new_series['USA']}")
print("Operations based on Series \n")
print(new_series + new_series_2)
