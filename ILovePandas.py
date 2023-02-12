import pandas as pd


cs1_df = pd.read_csv('C:\downloads\MyCSVFile1.csv')
print(cs1_df) 
cs2_df = cs1_df.T # Transpose dataframe
print(cs2_df)

cs2_df.to_csv('C:\downloads\MyCSVFile2.csv',header=False)  # Remove header line, write to new file
#print(cs_df['Amount'].mean())
#print (cs_df.describe)