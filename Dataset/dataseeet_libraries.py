import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Dataset\Online Sales Data.csv")

x = dataset.iloc[0].iloc[0]
y = dataset.iloc[:,0].values

print(x)    
#print(dataset)