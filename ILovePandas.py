import pandas as pd

cs_df = pd.read_csv('C:\downloads\MyStmt.csv')
#print(cs_df) 
print(cs_df['Amount'].min())
#print (cs_df.describe)