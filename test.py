import pickle
import pandas as pd
import numpy as np
import random
model = pickle.load(open('wheat_yield_prediction_model.pkl', 'rb'))
dataset_columns = ['Temperature','Humidity','Moisture','Rainfall','pH']
temperature = round(random.uniform(20,25), 3)
humidity = round(random.uniform(9,15), 3)
moisture = round(random.uniform(100,170), 2)
pH = round(random.uniform(6.1,6.9), 2)
data = {}
data[dataset_columns[0]]=temperature
data[dataset_columns[1]]=humidity
data[dataset_columns[2]]=moisture
data[dataset_columns[3]]=87.814740
data[dataset_columns[4]]=pH

# Convert dictionary to dataframe
df = pd.DataFrame(data, columns=dataset_columns,index=[0])
predictions = model.predict(df)
print(predictions[0])
