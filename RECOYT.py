import pandas as pd 
DF=pd.read_csv('GBvideos.csv')
print(len(DF.index))

print(DF['tags'].head())
import string
DF['ntags']=DF['tags'].str.repacle('[{}]'.format(string.punctuation),' ')
print(DF['ntags'].head())
