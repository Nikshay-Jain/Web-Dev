import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(334,5) , index=np.arange(334))

#use df.copy() to make a copy of data frame else original df will be changed on manipulating any of them
#we can also use df.loc[0,0] = 654 to change value at 0,0 to 654
#But, if column names are changed as shown:
df.columns = list("ABCDE")
print('\nChanged column names head:\n',df.head())

df.loc[0,0] = 654
print('\n\nManipulated data head:\n',df.head())
#ie, new column '0' created. So, use:

df.loc[0,'A']=654
df = df.drop(0 , axis=1)
print('\n\nDropping last rows 0:\n',df)
#if not mentioned df = df... , the change would be temporary, limited to that step only
#axis = 1 means remove column else 0 means row. Default is 0
#can drop mult too as df.drop(['A','C'], axis=1) drops both A and C together
#adding inplace=True will modify original itself, ie df.drop(['A','C'], axis=1, inplace=True)

df.drop([1,5],axis=0,inplace=True)
print('\n\nDropping rows 1 and 5:\n',df)

#Resets the index in order
df.reset_index(drop=True , inplace=True)
print('\n\nReset index:\n',df)

#Custom Filtering of rows and columns
print('\n\nFiltering data by row and column names:\n',df.loc[[1,2],['C','D']])

print('\n\nFiltering data by column value conditions:\n',df.loc[(df['A']<0.3) & (df['C']>0.4)])

print('\n\nFiltering out element from data by index:\n',df.iloc[0,4])      #gives same output as [0,'E'] ie, if you wanna use index, use iloc

#Custom rows and columns by indices
print('\n\nFiltering data by row and column indices:\n',df.iloc[[1,5],[0,2]])

print('\n\nChecking col B for nullity head:\n',df['B'].isnull().head())

df.loc[:,['B']]=None     #or use df['B']=None
print('\n\nSet col B as None:\n',df)
print('\n\nChecking col B for nullity head:\n',df['B'].isnull().head())
print()