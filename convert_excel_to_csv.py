import pandas as pd

# Download excel file from https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip

# Read both sheets from the Excel file
df_2009_2010 = pd.read_excel(
    '/home/ctyce/retail-demand-forecasting/data/online_retail_II.xlsx',
    sheet_name='Year 2009-2010'
)
df_2010_2011 = pd.read_excel(
    '/home/ctyce/retail-demand-forecasting/data/online_retail_II.xlsx',
    sheet_name='Year 2010-2011'
)

# Concatenate the dataframes
combined_df = pd.concat([df_2009_2010, df_2010_2011], ignore_index=True)

combined_df['InvoiceDate'] = pd.to_datetime(combined_df['InvoiceDate'])
combined_df = combined_df.sort_values('InvoiceDate')

# Save to CSV
combined_df.to_csv(
    '/home/ctyce/retail-demand-forecasting/data/online_sales_dataset.csv',
    index=False
)

print(f"Total rows processed: {len(combined_df)}")
print(f"Date range: {combined_df['InvoiceDate'].min()} to {combined_df['InvoiceDate'].max()}")
print(f"Number of unique products: {combined_df['StockCode'].nunique()}")
