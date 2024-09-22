import pandas as pd
import csv


def read_csv_file(path_to_file: str) -> dict:
    """Обработка csv файла в список словарей, указать путь к файлу"""
    df = pd.read_csv(f"{path_to_file}")
    df_dict = df.to_dict(orient='records')
    return df_dict


def read_excel_file(path_to_file: str) -> dict:
    """Обработка excel файла в список словарей, указать путь к файлу"""
    df = pd.read_excel(f"{path_to_file}")
    df_dict = df.to_dict(orient='records')
    return df_dict


#print(read_csv_file("../data/transactions.csv"))
#print(read_excel_file("transactions_excel.xlsx"))
