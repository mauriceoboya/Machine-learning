from data_ingestion import Importdata,logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

logging.info("Loading data...")
data=Importdata.read_data()

class DataPreprocessing:
    try:
        @staticmethod
        def clean(data):
            logging.info("Data cleaning...")
            x,y= data.drop(columns=['Class']),data['Class']
            strx=StandardScaler()
            x=strx.fit_transform(x)
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True)
            logging.info("Training model...")
            logist_model=LogisticRegression()
            logist_model.fit(x_train,y_train)
            y_pred=logist_model.predict(x_test)
            accuracy=confusion_matrix(y_test,y_pred)
            accuracy_plot=sns.heatmap(accuracy,annot=True, cmap="YlGnBu")
            plt.savefig('./confusion_matrix.png')
            return 'confusion_matrix.png'
    except Exception as e:
        logging.error(f"An error occurred: {e}")



if __name__ == '__main__':
    model = DataPreprocessing.clean(data)
    if model is not None:
        print(model)
    else:
        print("Failed model ingestion stage.")
