# Project Title: Consumer Price Index (CPI) Analysis for Rwanda

## Description
Welcome to the CPI Analysis for Rwanda project repository! This project focuses on cleaning and transforming the Consumer Price Index (CPI) data of Rwanda from February 2009 to March 2024 from an Excel file. In this repository, you'll find the necessary files and instructions to set up the project on your machine and perform data engineering tasks to extract meaningful insights from the dataset. The data source is in this excel file: [Consumer Price Index (CPI) Data](https://github.com/Sopho-Ngak/Consumer-Price-Index-ETL/blob/main/data/source/CPI_time_series_March_2024.xls).

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributors](#contributing)


## Requirements 
| Requirements | Version |
| ----------- | ------- |
| Python      | >=3.8   |
| Pandas      | >=2.2.2 |
| xlrd        | >=2.0.1 |


## Project Structure
The project is structured as follows:
```
Consumer-Price-Index-ETL/
│   data/
│   │   source/
│   │   │   CPI_time_series_March_2024.xls
│   │   transformed/
│   │   │   CPI_time_series.csv
│   │   data_by_source/
│   │   │   All Rwanda.csv
│   │   │   Rural.csv
│   │   │   Urban.csv
│   .gitignore
|   etl.py
│   main.py
│   README.md 
│   requirements.txt
```


## Installation
To setup the project on local machine, you need to follow these steps:
1. Clone the repository to your local machine using the following command:
```bash
git clone git@github.com:Sopho-Ngak/Consumer-Price-Index-ETL.git
```
or using HTTPS:
```bash
git clone https://github.com/Sopho-Ngak/Consumer-Price-Index-ETL.git
```

2. Create a virtual environment and activate using the following command:
```bash
python3 -m venv venv && source venv/bin/activate
```
3. Install the required Python packages using the following command:
```bash
cd Consumer-Price-Index-ETL
pip install -r requirements.txt
```

## Usage
To use the project, you need to follow these steps:
1. Run the ETL pipeline to extract, transform, and load the data using the following command:
```bash
python main.py
```
2. The output is saved in the `data/data_by_source` directory as CSV files named `All Rwanda.csv`, `Rural.csv` and `Urban.csv`. The final combined dataset will be saved as `CPI_time_series.csv` in the `data/transformed` directory.


### Contributors
[Sophonie Ngakoutou](https://github.com/Sopho-Ngak)