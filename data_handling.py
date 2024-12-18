import pandas as pd

class DataHandler:
    def __init__(self, data_file):
        self.data_file = data_file

    def load_data(self):
        return pd.read_csv(self.data_file)
