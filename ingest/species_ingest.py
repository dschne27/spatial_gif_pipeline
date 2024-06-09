'''Runs the species ingestion process.'''
from multiprocessing import Pool, set_start_method
import pandas as pd
from loguru import logger
from ingest.s3_utils import get_parquet_data

def main():
    '''Run the species ingestion process.'''
    logger.info("Loading all mammals data ...")
    results = []
    datasets = ['MAMMALS', 'PLANTS']
    with Pool(2) as pool:
        results = pool.map_async(get_parquet_data, datasets)
        results = [r for r in results.get()]
    mammals: pd.DataFrame | None = results[0]
    plants: pd.DataFrame | None = results[1]
    if mammals is not None:
        logger.info("Showing mammals.head():")
        print(mammals.head())
    if plants is not None:
        logger.info("Showing plants.head():")
        print(plants.head())
    else:
        logger.error("No data found.")
    print("species ingestion exit")
    

if __name__ == "__main__":
    set_start_method("spawn")
    main()

