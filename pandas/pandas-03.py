import numpy as np
import pandas as pd

my_data = np.random.randint(101, size =(3,4))
#print(my_data)

my_column_names = ['Eleanor','chidi','Tahani','Jason']

my_dataframe = pd.DataFrame(data = my_data, columns = my_column_names)

print(my_dataframe)

print()
print(my_dataframe.iloc[1]['Eleanor'])

my_dataframe['Janet'] = my_dataframe['Tahani'] + my_dataframe['Jason']

print(my_dataframe)
