import pandas as pd

input_file_name = input("Enter the input file name (with extension, e.g., input_file.csv): ")
df = pd.read_csv(input_file_name)
df_first_column = df.iloc[:, :1]
df_first_column = '|' + df_first_column.astype(str) + '|'
output_file_name = input("Enter the output file name (with extension, e.g., output_file.csv): ")

df_first_column.to_csv(output_file_name, index=False, header=False)

print(df_first_column)