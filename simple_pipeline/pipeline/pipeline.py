import sys
import pandas as pd
import numpy as np
import logging


logging.basicConfig(level=logging.INFO)
day = pd.Timestamp.now().strftime("%Y-%m-%d")
logging.info(f"Processing data for {day}")

df = pd.read_excel(r"C:\Users\Anthony\Pictures\data_engineering\simple_pipeline\data\md_water_service.xlsx")
print(df.head())

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.dayofweek

def process_data(df):
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in num_cols:
        df[col] = df[col].fillna(df[col].mean())

    cat_cols = df.select_dtypes(include=[object]).columns.tolist()
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Additional processing steps can be added here
    df['biological'] = df['biological'].round(2)
    return df

df = process_data(df)

df.to_csv(f"{r'C:\Users\Anthony\Pictures\data_engineering\simple_pipeline\data\csv_processed_data_{day}.csv'}", index=False )