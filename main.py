import pandas as pd
from etl import ETL, log

if __name__ == '__main__':
    log.info('===> Starting ETL process............')
    etl = ETL()
    # Extract data from the excel file
    df_dict: dict[str, pd.DataFrame] = etl.extract()

    # Transform the data
    df = etl.transform(df_extracted=df_dict)

    # Load the data to a CSV file
    etl.load(df=df)
    log.info('===> ETL process completed successfully............')