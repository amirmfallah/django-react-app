import pandas as pd

def open_file(file_path):
  if(file_path.endswith('.xls') or file_path.endswith('.xlsx')):
    return pd.read_excel(file_path)

  return pd.read_csv(file_path)

