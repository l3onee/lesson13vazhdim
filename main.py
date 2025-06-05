import pandas as pd
data = {
    "Germany,France,Portugal"
}

df =pd.read_csv('avgIQpercountry.csv') 
print(df.info())

print_rows = df.head() 

subset = df[['Country','Average IQ']]
print(subset)

filtered_df = df[['Average IQ'] < 100]
print(filtered_df)


# products = ['apple', 'banana', 'orange', 'grape']
# sales = [90,100,110,120]

# sales_index = pd.Series(sales,index=products)
# print(sales_index)

# sales_series = pd.Series(sales,index=products)
# print(sales_series)

# print(sales_series['grape'])

# total_sales = sales_series.sum()
# print(total_sales)

# # data={

# # df = pd.DataFrame(data)
# #     'Name': ['Leon','Darsej','Qamil'],
# #     'Age' : [25,2,88],
# #     'City' : ['Ferizaj','Gjakove','New Jesey']
# # }
# # print(df)

# # df = pd.DataFrame(pd)
# # print(df)

# # df = pd.read_csv('cs.csv')
# # df.to_csv('leon.csv', index= False)

# best_selling_product = total_sales.idxmax()
# print(f"Best selling product is: {best_selling_product}")