



import pandas as pd
import numpy as np

df = pd.read_csv('data/sales_records.csv')

# print(df.shape)       # e.g., (15420, 12)
print(df.dtypes)
# print(df.head())
# print(df.describe())
# print(df.isnull().sum())
# print(df.columns)

print(df.columns)

df.columns = ['_'.join(col.strip().lower().split(' ')).replace('(', '').replace(')', '') for col in df.columns.tolist()]
print(df.columns)

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['rev_usd'] = pd.to_numeric(df['rev_usd'], errors='coerce')


revenue = df['rev_usd']
subset = df[['customer_id', 'rev_usd', 'region']]

high_value = df.loc[df['rev_usd'] > 10000, ['customer_id', 'rev_usd']]
sample = df.iloc[:100, :4]

filtered = df[(df['region'] == 'North') & (df['rev_usd'] > 5000)]
filtered_v2 = df.query("region == 'North' and rev_usd > 5000")

df[df['status'].isin(['active', 'trial'])]

