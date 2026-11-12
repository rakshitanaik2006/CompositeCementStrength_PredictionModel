# Step 2 : Data Preprocessing And Cleaning

def data_preprocessing(df):
  '''
  Step1: Feature Engineering and Selection

  Step2: Split the dataset into independent and dependent columns i.e X and y

  Step3: Use train and test split i.e. split the dataset into Seen and Unseen
  (Seen Data: train data and Unseen Data: test data)

  Step4: Use Scaling Technique/ Normalization Technique
  (standardScaler/MinMaxScaler/RobustScaler)

  Step5: Return Seen and Unseen Data

  '''
  # Step1: Feature Engineering : Create a new feature based on existing feature

  df['Water  (component 4)(kg in a m^3 mixture)'] = df['Water  (component 4)(kg in a m^3 mixture)'] / (df['Cement (component 1)(kg in a m^3 mixture)'] + df['Blast Furnace Slag (component 2)(kg in a m^3 mixture)'] + df['Fly Ash (component 3)(kg in a m^3 mixture)'] )

  # Step2: Split the dataset into X and y
  target_col = 'Concrete compressive strength(MPa, megapascals) '
  X = df.drop(columns = [target_col]) # Independent Columns
  y = df[target_col]                  # Target Column

  #Step3: Split the dataset into Seen and Unseen (Train and Test Data)
  from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                      test_size=0.3,
                                                      random_state=1)

  X_train.shape, X_test.shape, y_train.shape, y_test.shape

  # Step4: Use Scaling / Normalization Technique
  '''
  * Scaling for training data: fit_transform()

  * Scaling for testing data: transform()

  '''
  sc = MinMaxScaler()
  X_train = sc.fit_transform(X_train)  # Seen Data
  X_test = sc.transform(X_test)        # UnSeen Data

 # Step5: Return seen and unseen data
  return X_train, X_test, y_train, y_test