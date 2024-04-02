import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s', filename='./logs.log')

class Importdata:
    @staticmethod
    def read_data():
        try:
            dataset = pd.read_csv('./Raisin_Dataset.csv')
            dataset['Class'] = dataset['Class'].apply(lambda x: 1 if x == "Kecimen" else 0)
            logging.info(f"data ingestion intiated")
            return dataset
            
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            return None
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return None
    

if __name__ =='__main__':
    data = Importdata.read_data()
    if data is not None:
        print(data)
    else:
        print("Failed to read data.")
