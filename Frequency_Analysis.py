import pandas as pd

pd.set_option('display.float_format', '{:.2f}'.format)
freq_df=pd.read_excel("Frequency_of_Purchase_Analysis_Data_Question.xlsx",usecols= "A:D")
count= freq_df.groupby('Outlet ID')['Outlet ID'].count().sort_values().reset_index(name='Count').set_index('Outlet ID')
print(count)
#count= freq_df.value_counts('Outlet ID').reset_index(name='Count')
No_of_Outlets= count.value_counts('Count').sort_values()    # Number of Outlets
print(No_of_Outlets)

merged_df= freq_df.merge(count, how="inner", on="Outlet ID")
print(merged_df)

total_sales_value= merged_df.groupby('Count').agg({"Sales Value":"sum"})  # Total Sales
print(total_sales_value)


