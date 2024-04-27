import os
import sys
import logging
import pandas as pd

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(filename)s - %(levelname)s -: %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
exele_path = os.path.join(BASE_DIR, 'data', 'source',
                          'CPI_time_series_March_2024.xls')
sheet_names = [
    'Urban',
    'Rural',
    'All Rwanda'
]


class ETL:
    def __init__(self, path: str = exele_path):
        self.path = path

    def extract(self) -> dict[str, pd.DataFrame]:
        '''
        Loop through all sheets in the excel file and return a dict of dataframes
        :return: dict of dataframes
        '''
        df_dict = {}
        xls = pd.ExcelFile(self.path)
        log.info(f'===> Extracting data from {self.path}')

        for sheet_name in xls.sheet_names:
            if sheet_name not in sheet_names:
                continue

            df_dict[sheet_name] = pd.read_excel(xls, sheet_name, skiprows=3)

        log.info(
            f'===> Extracted {len(df_dict)} sheets ({sheet_names}) from {self.path}')
        return df_dict

    def transform(self, df_extracted: dict[str, pd.DataFrame]) -> pd.DataFrame:
        '''
        Transform the data by removing unnecessary columns and rows
        :param df_dict: dict of dataframes
        :return: pd.DataFrame
        '''

        def transform_values(data: str) -> str:
            '''
            Remove occurrences of 'v' from the data
            :param data: str
            :return: str
            '''
            if 'v' in data[:3] and not data[1].isalpha():
                data = data[2:].strip()
                return data

            return data

        df_dict = {}
        log.info('===> Transforming data................')
        for key, df in df_extracted.items():

            data: pd.DataFrame = df
            data = data.rename(columns={
                'Unnamed: 0': 'Province',
                'Unnamed: 1': 'U_R',
                'Unnamed: 2': 'COICOP',
                'Unnamed: 3': 'Products'
            })

            # Remove missing values
            data = data.dropna(how='any')

            # Transform the dataset from a Wide format into a Long format
            df_melted = data.melt(id_vars=[
                                  'Province', 'U_R', 'COICOP', 'Products', 'Weights'], var_name='Date', value_name='Index')
            df_melted['Date'] = pd.to_datetime(df_melted['Date'])
            df_melted['Products'] = df_melted['Products'].apply(transform_values)

            df = df_melted
            del df_melted
            df['Source'] = key
            df_dict[key] = df

            df.to_csv(os.path.join(BASE_DIR, 'data',
                      'data_by_source', f'{key}.csv'), index=False)

        log.info('............Transformation complete..............')
        # Concatenate the dataframes into a single dataframe
        df_final = pd.concat(df_dict.values())

        return df_final

    def load(self, df: pd.DataFrame = None):
        log.info('===> Loading data to CSV file............')
        df.to_csv(os.path.join(BASE_DIR, 'data',
                  'transformed', 'CPI_time_series.csv'), index=False)
        log.info('............Data loaded successfully............')


