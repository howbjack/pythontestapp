import pandas as pd

cs_df = pd.read_csv('C:\downloads\MyStmt.csv')
print(cs_df) 
print(cs_df['Amount'].mean())
#print (cs_df.describe)