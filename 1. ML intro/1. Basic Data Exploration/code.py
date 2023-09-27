import pandas as pd

# melbourne data snapshot, source: https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot 

melbourne_file_path = './input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

print(melbourne_data.head())

print(melbourne_data.describe())