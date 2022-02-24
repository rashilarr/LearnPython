import numpy as np
import pandas as pd

my_data = np.array([[0,3],[10,7],[20,9],[30,14],[40,15]])

my_column_names = ['Temperature','Activity']

my_dataframe = pd.DataFrame(data = my_data, columns = my_column_names)

#print(my_dataframe)

my_dataframe['Adjusted'] = my_dataframe['Activity'] + 2

#print(my_dataframe)

#print(my_dataframe.head(3), '\n') #to print first 3 rows
#print(my_dataframe.iloc[[2]])  # To print row#2
#print(my_dataframe[1:4]) # to print rows#1, row#2,row#3

print(my_dataframe['Temperature'])  # to print the column temperature


