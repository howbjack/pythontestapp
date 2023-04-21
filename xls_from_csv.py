import os
import pandas as pd
import openpyxl

# The read_csv is reading the csv file into Dataframe
# csvfolder = "S:\Smart Business Works\Expense Reports\2022"
# os.chdir(r"C:\downloads")
# csvfile = '1_2022.csv'

#csv_path = os.path.join('csvfolder', 'csvfile')
#print(f"The path is : {csv_path}")

df = pd.read_csv('C:\downloads\November2022.csv')
print(df.head)

# then to_excel method converting the .csv file to .xlsx file.
with pd.ExcelWriter('C:\downloads\TOLLS_2022.xlsx', mode='a') as writer:
    df.to_excel(writer, sheet_name="11_2022", index=False)
