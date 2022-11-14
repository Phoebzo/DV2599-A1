# Phoebe Waters DVAMI19h

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pip install pyqt5

#data processing

df = pd.read_csv("spambase.csv")


df = df.drop_duplicates()
df = df.reset_index()


def descretinization_3(column_list):
    mean = column_list.mean()
    std = column_list.std()
#high percentage = 1
#meadium = 0
#low = -1
    for index,value in column_list.items():
        if value > mean + std:
            column_list[index] = 1
        elif value < mean - std:
            column_list[index] = -1
        else:
            column_list[index] = 0

print(df['word_freq_make'])
descretinization_3(df['word_freq_make'])
print(df['word_freq_make'])

'''
for column in df:
    descretinization_3(df[column])
'''

descretinization_3(df['index'])
df['index'].plot(kind = 'hist')
plt.show()

