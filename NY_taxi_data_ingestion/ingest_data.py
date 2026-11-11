#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import click
import pandas as pd
import numpy as np
import os
from tqdm import tqdm


# In[11]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)
df.head()


# In[12]:


df.dtypes


# In[13]:


df.shape


# # CLICK INTEGRATION

# In[ ]:


@click.command()
@click.option('--pg-user', default='anthony', help='Database user')
@click.option('--pg-password', default='anthony', help='Database password')
@click.option('--pg-host', default='localhost', help='Database host')
@click.option('--pg-port', default=5432, help='Database port')
@click.option('--pg-database', default='ny_taxi', help='Database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
def main(pg_user, pg_password, pg_host, pg_port, pg_database, target_table):
    from sqlalchemy import create_engine
    engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}')

    dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]

    df = pd.read_csv(
        prefix + 'yellow_tripdata_2021-01.csv.gz',
        nrows=100,
        dtype=dtype,
        parse_dates=parse_dates
    )

    # create the table in the database
    df.head(n=0).to_sql(
        name=target_table,
        con=engine,
        if_exists='replace'
    )

    # Batch Iterator
    df_iter = pd.read_csv(
        prefix + 'yellow_tripdata_2021-01.csv.gz',
        iterator=True,
        chunksize=100000,
        dtype=dtype,
        parse_dates=parse_dates
    )

    # Insert data in chunks
    for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists='append'
        )
        print("Inserted Chunk of size: ", len(df_chunk))

if __name__ == '__main__':
    main()

