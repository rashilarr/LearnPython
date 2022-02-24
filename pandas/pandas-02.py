import numpy as np
import pandas as pd

my_data = np.array([['Akshara', 5],['Amisna',6],['Rithvi',9]])

my_column_names = ['Name', 'Age']

my_dataframe = pd.DataFrame(data = my_data, columns = my_column_names)

#print(my_dataframe)

my_dataframe['Grade'] = ['TK','Kindergarten', 'Third']
#print(my_dataframe)

print(my_dataframe.head(3), '\n')
