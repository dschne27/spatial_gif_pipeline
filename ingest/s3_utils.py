import os
import time
from dotenv import load_dotenv
import pandas as pd
import pyarrow.parquet as pq
import s3fs
from loguru import logger

load_dotenv()

S3_BUCKET = os.environ.get('S3_BUCKET')
AWS_REGION = os.environ.get('AWS_REGION')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_ACCESS_KEY_SECRET = os.environ.get('AWS_ACCESS_KEY_SECRET')

# Read the parquet file from S3
def get_s3_fs() -> s3fs.S3FileSystem:
    '''Connect to IUCN data S3 bucket.'''
    try:
        fs = s3fs.S3FileSystem(profile='default')
        return fs
    except EnvironmentError:
        print("No AWS credentials found. Please set the AWS_ACCESS_KEY_ID \
                and AWS_ACCESS_KEY_SECRET environment variables.")

def get_parquet_data(dataset_name: str) -> pd.DataFrame:
    '''Read all parquet files for a given IUCN dataset from S3 bucket.'''
    try:
        fs = get_s3_fs()
        dataset_base_dir = f's3://{S3_BUCKET}/{dataset_name}/'
        all_dataset_parquet_files = fs.glob(f"{dataset_base_dir}*.parquet")
        logger.info(f"Found {len(all_dataset_parquet_files)} parquet files in {dataset_base_dir}")

        file_list = [f's3://{file}' for file in parquet_files]

        start_time = time.time()
        logger.info(f"Reading parquet data from {parquet_base_dir}")

        dataset = pq.ParquetDataset(file_list, filesystem=fs)
        table = dataset.read()
        dataframe = table.to_pandas()

        end_time = time.time()
        logger.info(f"Read {len(dataframe)} records from dataset {dataset_name} in {end_time - start_time} seconds")
        return dataframe
    except Exception as e:
        logger.error(f"Error reading parquet data: {e}")
        return None
        