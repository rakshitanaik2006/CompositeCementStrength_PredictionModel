from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing
from src.model_build import model_building

# Define Orchestron Model: Entry Point
def main():     #Function Definition
  #Steps1: Data Ingestion
  df = data_ingestion()
  #Step2: Data Preprocessing and Cleaning
  X_train,X_test,y_train,y_test = data_preprocessing(df)
  #Step3:Model Building
  score = model_building(X_train,X_test,y_train,y_test)
  print(f'R2 Score : {score}')



main()         #Function Calling